import Foundation
import Network

@MainActor
class RAGService: ObservableObject {
    private var listener: NWListener?
    private var connection: NWConnection?
    private var process: Process?
    private var flaskProcess: Process?
    private var port: NWEndpoint.Port?
    private var responseCallbacks: [Int: (([String]) -> Void)] = [:]
    private var requestId = 1
    private var tcpBuffer: String = ""
    
    static let shared = RAGService()
    
    private init() {
        startTCPServerAndSpawnDaemon()
        spawnFlaskBackend()
    }
    
    /// Binds local TCP server to an ephemeral port and spawns the background Python daemon.
    func startTCPServerAndSpawnDaemon() {
        do {
            // Bind to 127.0.0.1 on port 0 to allocate an ephemeral free port
            listener = try NWListener(using: .tcp, on: .any)
            
            listener?.stateUpdateHandler = { [weak self] state in
                guard let self = self else { return }
                Task { @MainActor in
                    switch state {
                    case .ready:
                        if let allocatedPort = self.listener?.port {
                            self.port = allocatedPort
                            // Ephemeral port allocated! Spawn the Python RAG daemon now.
                            self.spawnPythonDaemon(port: allocatedPort.rawValue)
                        }
                    default:
                        break
                    }
                }
            }
            
            listener?.newConnectionHandler = { [weak self] newConnection in
                guard let self = self else { return }
                Task { @MainActor in
                    self.connection = newConnection
                    self.connection?.stateUpdateHandler = { state in
                        Task { @MainActor in
                            switch state {
                            case .ready:
                                self.receiveNextMessage()
                            default:
                                break
                            }
                        }
                    }
                    self.connection?.start(queue: .global(qos: .userInteractive))
                }
            }
            
            listener?.start(queue: .global(qos: .userInitiated))
            
        } catch {
            print("Failed to initialize local TCP server for RAG daemon.")
        }
    }
    
    private func spawnPythonDaemon(port: UInt16) {
        let process = Process()
        self.process = process
        
        process.executableURL = URL(fileURLWithPath: "/Users/justin/python-ai-academy/.venv/bin/python")
        // CRITICAL FIX: Pass absolute script path to guarantee successful boot from Xcode DerivedData
        process.arguments = ["/Users/justin/python-ai-academy/backend/rag_daemon.py", String(port)]
        process.currentDirectoryURL = URL(fileURLWithPath: "/Users/justin/python-ai-academy")
        
        var environment = ProcessInfo.processInfo.environment
        environment["PYTHONUNBUFFERED"] = "1"
        process.environment = environment
        
        do {
            try process.run()
        } catch {
            print("Failed to spawn Python RAG daemon.")
        }
    }
    
    /// Automatically spawns our Flask backend server on local port 5000 inside its own POSIX Process Group.
    private func spawnFlaskBackend() {
        let process = Process()
        self.flaskProcess = process
        
        process.executableURL = URL(fileURLWithPath: "/Users/justin/python-ai-academy/.venv/bin/python")
        // CRITICAL FIX: Pass absolute script path to guarantee successful boot from Xcode DerivedData
        process.arguments = ["-u", "/Users/justin/python-ai-academy/backend/main.py"]
        process.currentDirectoryURL = URL(fileURLWithPath: "/Users/justin/python-ai-academy")
        
        var environment = ProcessInfo.processInfo.environment
        environment["PYTHONUNBUFFERED"] = "1"
        environment["PYTHONPATH"] = "/Users/justin/python-ai-academy"
        process.environment = environment
        
        do {
            try process.run()
            // Isolate Flask and its children in their own Process Group
            let pid = process.processIdentifier
            setpgid(pid, pid)
        } catch {
            print("Failed to auto-spawn local Flask backend server.")
        }
    }
    
    private func receiveNextMessage() {
        guard let connection = connection else { return }
        
        connection.receive(minimumIncompleteLength: 1, maximumLength: 65536) { [weak self] (data, _, isComplete, error) in
            guard let self = self else { return }
            
            Task { @MainActor in
                if let data = data, !data.isEmpty {
                    self.processIncomingData(data)
                }
                
                if isComplete {
                    return // EOF
                }
                if error != nil {
                    return
                }
                
                self.receiveNextMessage() // Loop
            }
        }
    }
    
    private func processIncomingData(_ data: Data) {
        guard let stringChunk = String(data: data, encoding: .utf8) else { return }
        tcpBuffer += stringChunk
        
        // Process complete lines delimited by \n (TCP Framing)
        while let newlineIndex = tcpBuffer.firstIndex(of: "\n") {
            let line = String(tcpBuffer[..<newlineIndex]).trimmingCharacters(in: .whitespacesAndNewlines)
            tcpBuffer = String(tcpBuffer[tcpBuffer.index(after: newlineIndex)...])
            
            if line.isEmpty { continue }
            
            guard let lineData = line.data(using: .utf8),
                  let json = try? JSONSerialization.jsonObject(with: lineData, options: []) as? [String: Any] else {
                continue
            }
            
            if let reqId = json["id"] as? Int, let result = json["result"] as? [String] {
                if let callback = self.responseCallbacks.removeValue(forKey: reqId) {
                    callback(result)
                }
            }
        }
    }
    
    /// Queries the local RAG daemon asynchronously, returning top semantic matches.
    func queryRAG(query: String) async -> [String] {
        guard let connection = connection else {
            return ["RAG daemon offline: Local connection is establishing..."]
        }
        
        let reqId = requestId
        requestId += 1
        
        let request: [String: Any] = [
            "jsonrpc": "2.0",
            "method": "search",
            "params": ["query": query],
            "id": reqId
        ]
        
        guard let requestData = try? JSONSerialization.data(withJSONObject: request, options: []),
              let requestString = String(data: requestData, encoding: .utf8) else {
            return ["Error: Failed to serialize JSON-RPC RAG request."]
        }
        
        return await withCheckedContinuation { continuation in
            responseCallbacks[reqId] = { result in
                continuation.resume(returning: result)
            }
            
            let payload = requestString + "\n"
            connection.send(content: payload.data(using: .utf8), completion: .contentProcessed({ error in
                if let error = error {
                    print("RAG TCP Send Error: \(error)")
                    continuation.resume(returning: ["RAG transmission pipeline error."])
                }
            }))
        }
    }
    
    /// Cleans up and terminates both RAG and Flask background process groups immediately.
    func terminateAllServices() {
        connection?.cancel()
        listener?.cancel()
        
        // 1. Terminate the Python RAG daemon
        if let process = process, process.isRunning {
            process.terminate()
        }
        
        // 2. Forcefully kill the entire Flask backend POSIX process group
        if let flaskProcess = flaskProcess, flaskProcess.isRunning {
            let pid = flaskProcess.processIdentifier
            Darwin.kill(-pid, SIGKILL)
        }
    }
}
