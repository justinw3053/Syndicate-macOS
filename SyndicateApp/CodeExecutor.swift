import Foundation
import Darwin

class CodeExecutor {
    private var process: Process?
    private var watchdogItem: DispatchWorkItem?
    private var isCompleted = false
    private let lock = NSLock()
    
    /// Executes the student's code concatenated with assertions inside a dedicated process group.
    /// Runs asynchronously on a background thread and streams merged stdout/stderr back to the caller.
    func execute(
        code: String,
        assertions: String,
        workspacePath: String = "/Users/justin/python-ai-academy",
        onOutput: @escaping (String) -> Void,
        onCompletion: @escaping (Bool) -> Void
    ) {
        lock.lock()
        // Cancel any existing running processes first and reset completed latch
        terminateActiveProcess()
        self.isCompleted = false
        lock.unlock()
        
        let activeLabPath = "\(workspacePath)/active_lab.py"
        let verifyLabPath = "\(workspacePath)/verify_lab.py"
        let pythonInterpreterPath = "\(workspacePath)/.venv/bin/python"
        
        // 1. Write student's code to active_lab.py
        do {
            try code.write(toFile: activeLabPath, atomically: true, encoding: .utf8)
        } catch {
            onOutput("Error: Failed to write active_lab.py to workspace.\n")
            triggerCompletion(false, onCompletion: onCompletion)
            return
        }
        
        // 2. Construct the verify_lab.py script containing user code + assertions
        let mergedCode = """
# -*- coding: utf-8 -*-
import sys
import os

# Ensure .pi is in sys.path so progress tracking works natively
pi_path = os.path.join("\(workspacePath)", ".pi")
if pi_path not in sys.path:
    sys.path.append(pi_path)

# --- Student Code ---
\(code)

# --- Hidden Assertions ---
\(assertions)
"""
        do {
            try mergedCode.write(toFile: verifyLabPath, atomically: true, encoding: .utf8)
        } catch {
            onOutput("Error: Failed to write verify_lab.py to workspace.\n")
            triggerCompletion(false, onCompletion: onCompletion)
            return
        }
        
        // 3. Configure the Process
        let process = Process()
        self.process = process
        
        process.executableURL = URL(fileURLWithPath: pythonInterpreterPath)
        process.arguments = ["-u", verifyLabPath]
        process.currentDirectoryURL = URL(fileURLWithPath: workspacePath)
        
        var environment = ProcessInfo.processInfo.environment
        environment["PYTHONUNBUFFERED"] = "1"
        environment["PYTHONPATH"] = "\(workspacePath):\(workspacePath)/.pi"
        process.environment = environment
        
        // 4. Create the I/O Pipes
        let outputPipe = Pipe()
        process.standardOutput = outputPipe
        // Merge standard error into standard output at the OS level for perfect chronological ordering
        process.standardError = outputPipe
        
        let readHandle = outputPipe.fileHandleForReading
        
        readHandle.readabilityHandler = { handle in
            let data = handle.availableData
            if data.isEmpty {
                handle.readabilityHandler = nil
                return
            }
            if let outputString = String(data: data, encoding: .utf8) {
                onOutput(outputString)
            }
        }
        
        // 5. Start the execution
        do {
            try process.run()
            
            // Create a separate process group
            let pid = process.processIdentifier
            setpgid(pid, pid)
            
        } catch {
            onOutput("Error: Failed to spawn Python interpreter subprocess. Verify your virtual environment.\n")
            triggerCompletion(false, onCompletion: onCompletion)
            return
        }
        
        // 6. Set up the 5-Second Watchdog Timer
        let watchdog = DispatchWorkItem { [weak self, weak process] in
            guard let self = self, let activeProcess = process, activeProcess.isRunning else { return }
            
            let pid = activeProcess.processIdentifier
            
            // Send SIGTERM to the entire negative process group ID to cleanly stop parents and children
            Darwin.kill(-pid, SIGTERM)
            onOutput("\n[TIMEOUT] CPU limit exceeded. Terminating loop hierarchy (SIGTERM)...\n")
            
            // Wait 500ms and send SIGKILL to guarantee absolute destruction
            DispatchQueue.global().asyncAfter(deadline: .now() + 0.5) {
                if activeProcess.isRunning {
                    Darwin.kill(-pid, SIGKILL)
                    onOutput("[TIMEOUT] Force killed (SIGKILL) unresponsive process group.\n")
                }
            }
            
            self.triggerCompletion(false, onCompletion: onCompletion)
        }
        self.watchdogItem = watchdog
        DispatchQueue.global().asyncAfter(deadline: .now() + 5.0, execute: watchdog)
        
        // 7. Monitor process completion
        process.terminationHandler = { [weak self] completedProcess in
            guard let self = self else { return }
            
            lock.lock()
            self.watchdogItem?.cancel()
            self.watchdogItem = nil
            lock.unlock()
            
            try? FileManager.default.removeItem(atPath: verifyLabPath)
            
            let exitCode = completedProcess.terminationStatus
            let success = (exitCode == 0)
            
            self.triggerCompletion(success, onCompletion: onCompletion)
        }
    }
    
    private func triggerCompletion(_ success: Bool, onCompletion: @escaping (Bool) -> Void) {
        lock.lock()
        defer { lock.unlock() }
        
        guard !isCompleted else { return }
        isCompleted = true
        onCompletion(success)
    }
    
    /// Forcefully terminates any currently active process and cancels its watchdog.
    func terminateActiveProcess() {
        watchdogItem?.cancel()
        watchdogItem = nil
        
        if let activeProcess = process, activeProcess.isRunning {
            let pid = activeProcess.processIdentifier
            Darwin.kill(-pid, SIGKILL)
            process = nil
        }
    }
    
    deinit {
        terminateActiveProcess()
    }
}
