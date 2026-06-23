import SwiftUI

struct ContentView: View {
    @StateObject private var syllabusVM = SyllabusViewModel()
    @StateObject private var chatVM = ChatViewModel()
    
    var body: some View {
        HSplitView {
            // Left Column: Syllabus Map Sidebar
            SyllabusSidebarView(viewModel: syllabusVM)
                .background(
                    Group {
                        if syllabusVM.activeTheme == .systemGlass {
                            VisualEffectView(material: .sidebar, blendingMode: .behindWindow)
                        } else {
                            syllabusVM.activeTheme.sidebarBackground
                        }
                    }
                )
            
            // Center Column: The Forge (resizable split pane of markdown + code)
            ForgeEditorView(viewModel: syllabusVM)
                .frame(minWidth: 400, maxWidth: .infinity)
                .background(
                    Group {
                        if syllabusVM.activeTheme == .systemGlass {
                            VisualEffectView(material: .windowBackground, blendingMode: .behindWindow)
                        } else {
                            syllabusVM.activeTheme.contentBackground
                        }
                    }
                )
            
            // Right Column: Socratic Chat Comms Array
            CommsArrayView(
                viewModel: chatVM,
                currentCode: syllabusVM.activeCode,
                lessonId: syllabusVM.selectedLesson?.id ?? "",
                syllabusVM: syllabusVM
            )
            .background(
                Group {
                    if syllabusVM.activeTheme == .systemGlass {
                        VisualEffectView(material: .hudWindow, blendingMode: .behindWindow)
                    } else {
                        syllabusVM.activeTheme.sidebarBackground
                    }
                }
            )
        }
        .frame(minWidth: 1100, minHeight: 700)
        .onAppear {
            // Eagerly initialize RAGService and auto-spawn background processes (Flask + Daemon) on app boot!
            _ = RAGService.shared
            _ = StateReceiver.shared // Eagerly boot UDF Receiver
            
            // Wire up UDF Event Bus Actions
            StateReceiver.shared.onLessonCompleted = { lessonId in
                Task {
                    await syllabusVM.fetchSyllabus()
                }
            }
            StateReceiver.shared.onThemeChanged = { themeName in
                if let newTheme = AppTheme(rawValue: themeName) {
                    syllabusVM.activeTheme = newTheme
                }
            }
            
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
