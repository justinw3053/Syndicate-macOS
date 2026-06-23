import Foundation
import Network
import Darwin

class CodeExecutor {
    private var daemonProcess: Process?
    private var listener: NWListener?
    private var connection: NWConnection?
    
    private var tcpBuffer: String = ""
    private var isCompleted = false
    private let lock = NSLock()
    
    private var onOutputCallback: ((String) -> Void)?
    private var onCompletionCallback: ((Bool) -> Void)?
    private var currentReqId = 1
    private var pendingRequestData: Data? = nil
    
    init() {
        startTCPServerAndSpawnDaemon()
    }
    
    private func startTCPServerAndSpawnDaemon() {
        do {
            // Bind to ephemeral port for internal IPC routing
            listener = try NWListener(using: .tcp, on: .any)
            listener?.stateUpdateHandler = { [weak self] state in
                guard let self = self else { return }
                if case .ready = state, let port = self.listener?.port {
                    self.spawnPythonDaemon(port: port.rawValue)
                }
            }
            listener?.newConnectionHandler = { [weak self] newConnection in
                guard let self = self else { return }
                self.connection = newConnection
                self.connection?.stateUpdateHandler = { state in
                    if case .ready = state {
                        self.receiveNextMessage()
                        self.sendPendingRequest()
                    }
                }
                self.connection?.start(queue: .global(qos: .userInteractive))
            }
            listener?.start(queue: .global(qos: .userInitiated))
        } catch {
            print("Failed to initialize execution daemon TCP server.")
        }
    }
    
    private func spawnPythonDaemon(port: UInt16) {
        let process = Process()
        self.daemonProcess = process
        
        let workspacePath = NSHomeDirectory() + "/python-ai-academy"
        
        // Use the hermetic Python environment packaged inside the app bundle
        var finalPythonPath = "\(workspacePath)/.venv/bin/python"
        if let resourceURL = Bundle.main.resourceURL {
            let pythonPath = resourceURL.appendingPathComponent("python_runtime/bin/python3").path
            if FileManager.default.fileExists(atPath: pythonPath) {
                finalPythonPath = pythonPath
            }
        }
            
        process.executableURL = URL(fileURLWithPath: finalPythonPath)
        process.arguments = ["\(workspacePath)/backend/code_execution_daemon.py", String(port)]
        process.currentDirectoryURL = URL(fileURLWithPath: workspacePath)
        
        var environment = ProcessInfo.processInfo.environment
        environment["PYTHONUNBUFFERED"] = "1"
        process.environment = environment
        
        do {
            try process.run()
            // Create a separate process group
            let pid = process.processIdentifier
            setpgid(pid, pid)
        } catch {
            print("Failed to spawn Python Exec daemon.")
        }
    }
    
    private func receiveNextMessage() {
        connection?.receive(minimumIncompleteLength: 1, maximumLength: 65536) { [weak self] (data, _, isComplete, error) in
            guard let self = self else { return }
            if let data = data, !data.isEmpty {
                self.processIncomingData(data)
            }
            if !isComplete && error == nil {
                self.receiveNextMessage()
            }
        }
    }
    
    private func processIncomingData(_ data: Data) {
        guard let stringChunk = String(data: data, encoding: .utf8) else { return }
        tcpBuffer += stringChunk
        
        // Process complete JSON-RPC messages framed by newline
        while let newlineIndex = tcpBuffer.firstIndex(of: "\n") {
            let line = String(tcpBuffer[..<newlineIndex]).trimmingCharacters(in: .whitespacesAndNewlines)
            tcpBuffer = String(tcpBuffer[tcpBuffer.index(after: newlineIndex)...])
            
            if line.isEmpty { continue }
            guard let lineData = line.data(using: .utf8),
                  let json = try? JSONSerialization.jsonObject(with: lineData, options: []) as? [String: Any] else {
                continue
            }
            
            if let output = json["output"] as? String {
                DispatchQueue.main.async {
                    self.onOutputCallback?(output)
                }
            }
            
            if let done = json["done"] as? Bool, done, let success = json["success"] as? Bool {
                triggerCompletion(success)
            }
        }
    }
    
    private func sendPendingRequest() {
        lock.lock()
        defer { lock.unlock() }
        if let data = pendingRequestData, connection?.state == .ready {
            connection?.send(content: data, completion: .contentProcessed({ _ in }))
            pendingRequestData = nil
        }
    }
    
    /// Executes the student's code asynchronously via the JSON-RPC daemon.
    func execute(
        code: String,
        assertions: String,
        workspacePath: String = NSHomeDirectory() + "/python-ai-academy",
        onOutput: @escaping (String) -> Void,
        onCompletion: @escaping (Bool) -> Void
    ) {
        lock.lock()
        self.onOutputCallback = onOutput
        self.onCompletionCallback = onCompletion
        self.isCompleted = false
        self.currentReqId += 1
        let reqId = self.currentReqId
        lock.unlock()
        
        let request: [String: Any] = [
            "jsonrpc": "2.0",
            "method": "execute",
            "params": [
                "code": code,
                "assertions": assertions,
                "workspacePath": workspacePath
            ],
            "id": reqId
        ]
        
        guard let requestData = try? JSONSerialization.data(withJSONObject: request, options: []),
              let requestString = String(data: requestData, encoding: .utf8),
              let finalData = (requestString + "\n").data(using: .utf8) else {
            onOutput("Error: Failed to serialize JSON-RPC execution request.\n")
            triggerCompletion(false)
            return
        }
        
        lock.lock()
        pendingRequestData = finalData
        lock.unlock()
        
        sendPendingRequest()
    }
    
    private func triggerCompletion(_ success: Bool) {
        lock.lock()
        defer { lock.unlock() }
        guard !isCompleted else { return }
        isCompleted = true
        DispatchQueue.main.async {
            self.onCompletionCallback?(success)
        }
    }
    
    /// Severs the callback hooks for the active execution (effectively abandoning it).
    func terminateActiveProcess() {
        lock.lock()
        self.onOutputCallback = nil
        self.onCompletionCallback = nil
        lock.unlock()
    }
    
    deinit {
        connection?.cancel()
        listener?.cancel()
        if let activeProcess = daemonProcess, activeProcess.isRunning {
            let pid = activeProcess.processIdentifier
            Darwin.kill(-pid, SIGKILL)
        }
    }
}
