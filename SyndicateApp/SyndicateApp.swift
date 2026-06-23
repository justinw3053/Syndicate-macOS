import SwiftUI

@main
struct OpenForgeApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    var body: some Scene {
        WindowGroup {
            ContentView().onAppear { _ = StateReceiver.shared }
        }
    }
}

class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationWillTerminate(_ notification: Notification) {
        // Clean up both the RAG Daemon and Flask Backend Process Groups immediately upon app close
        RAGService.shared.terminateAllServices()
    }
}
