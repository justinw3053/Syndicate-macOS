import SwiftUI

struct ContentView: View {
    @StateObject private var syllabusVM = SyllabusViewModel()
    @StateObject private var chatVM = ChatViewModel()
    
    var body: some View {
        HSplitView {
            // Left Column: Syllabus Map Sidebar (Vibrant Liquid Sidebar)
            SyllabusSidebarView(viewModel: syllabusVM)
                .background(VisualEffectView(material: .sidebar, blendingMode: .behindWindow))
            
            // Center Column: The Forge (Liquid Editor Stage)
            ForgeEditorView(viewModel: syllabusVM)
                .frame(minWidth: 400, maxWidth: .infinity)
                .background(VisualEffectView(material: .underWindowBackground, blendingMode: .behindWindow))
            
            // Right Column: Socratic Chat Comms Array (Liquid Socratic HUD)
            CommsArrayView(
                viewModel: chatVM,
                currentCode: syllabusVM.activeCode,
                lessonId: syllabusVM.selectedLesson?.id ?? ""
            )
            .background(VisualEffectView(material: .hudWindow, blendingMode: .behindWindow))
        }
        .frame(minWidth: 1100, minHeight: 700)
        .onAppear {
            // Eagerly initialize RAGService and auto-spawn background processes (Flask + Daemon) on app boot!
            _ = RAGService.shared
            
            Task {
                // Give the background Flask server a safe 500ms moment to bind to port 5050
                try? await Task.sleep(nanoseconds: 500_000_000)
                await syllabusVM.fetchSyllabus()
            }
        }
        // Non-destructive external modification conflict handler alert
        .alert("File Modified Externally", isPresented: $syllabusVM.showConflictModal) {
            Button("Keep My Changes") {
                syllabusVM.keepMyChanges()
            }
            Button("Load Disk Version") {
                syllabusVM.loadDiskVersion()
            }
            Button("Cancel", role: .cancel) {}
        } message: {
            Text("The file active_lab.py was modified in an external editor (VS Code/Vim). Would you like to keep your active local edits or reload the version saved on disk?")
        }
    }
}

// MARK: - Native macOS Translucency Helper
struct VisualEffectView: NSViewRepresentable {
    var material: NSVisualEffectView.Material
    var blendingMode: NSVisualEffectView.BlendingMode
    
    func makeNSView(context: Context) -> NSVisualEffectView {
        let view = NSVisualEffectView()
        view.material = material
        view.blendingMode = blendingMode
        view.state = .active
        return view
    }
    
    func updateNSView(_ nsView: NSVisualEffectView, context: Context) {
        nsView.material = material
        nsView.blendingMode = blendingMode
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
