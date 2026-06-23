import Foundation

@MainActor
class StateReceiver: ObservableObject {
    static let shared = StateReceiver()
    private var task: Task<Void, Never>?
    
    // UDF Subscription Callbacks
    var onLessonCompleted: ((String) -> Void)?
    var onThemeChanged: ((String) -> Void)?
    
    private init() {
        startListening()
    }
    
    func startListening() {
        task?.cancel()
        task = Task {
            guard let url = URL(string: "http://127.0.0.1:5050/api/events") else { return }
            var request = URLRequest(url: url)
            request.timeoutInterval = TimeInterval(INT_MAX)
            
            do {
                let (bytes, response) = try await URLSession.shared.bytes(for: request)
                guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else { return }
                
                for try await line in bytes.lines {
                    if line.hasPrefix("data: ") {
                        let jsonString = String(line.dropFirst(6))
                        guard let data = jsonString.data(using: .utf8),
                              let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                              let type = json["type"] as? String,
                              let payload = json["payload"] as? [String: Any] else { continue }
                        
                        await processEvent(type: type, payload: payload)
                    }
                }
            } catch {
                // Reconnect on failure after a brief delay
                try? await Task.sleep(nanoseconds: 2_000_000_000)
                startListening()
            }
        }
    }
    
    private func processEvent(type: String, payload: [String: Any]) async {
        switch type {
        case "lessonCompleted":
            if let lessonId = payload["lessonId"] as? String {
                self.onLessonCompleted?(lessonId)
            }
        case "themeChanged":
            if let themeName = payload["themeName"] as? String {
                self.onThemeChanged?(themeName)
            }
        default:
            break
        }
    }
    
    deinit {
        task?.cancel()
    }
}
