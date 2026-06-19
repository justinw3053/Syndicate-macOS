import SwiftUI

@main
struct SyndicateApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationWillTerminate(_ notification: Notification) {
        // Clean up both the RAG Daemon and Flask Backend Process Groups immediately upon app close
        RAGService.shared.terminateAllServices()
    }
}
