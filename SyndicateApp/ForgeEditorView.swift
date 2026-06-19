import SwiftUI

struct ForgeEditorView: View {
    @ObservedObject var viewModel: SyllabusViewModel
    @State private var consoleOutput: String = ""
    
    @State private var isVerifyHovered = false
    @State private var isResetHovered = false
    
    var body: some View {
        VSplitView {
            // Upper Panel: Discovery Lab Bento Card (Liquid Glass)
            VStack(spacing: 0) {
                BentoPanel(title: "Discovery Playbook", systemIcon: "safari.fill") {
                    if viewModel.activeContent != nil {
                        MarkdownWebView(markdown: viewModel.activeContent?.markdown ?? "")
                    } else {
                        VStack(spacing: 12) {
                            Spacer()
                            ProgressView()
                                .scaleEffect(0.8)
                            Text("Forging playbook...")
                                .font(.caption)
                                .foregroundColor(.secondary)
                            Spacer()
                        }
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                    }
                }
                .padding(.top, 16)
                .padding(.horizontal, 16)
                .padding(.bottom, 8)
            }
            .frame(minHeight: 200)
            
            // Lower Panel: Code Stage Bento Card & Terminal Console
            VStack(spacing: 0) {
                VStack(spacing: 12) {
                    // Bento Code Stage (Liquid Glass)
                    VStack(alignment: .leading, spacing: 0) {
                        // Header bar
                        HStack {
                            Image(systemName: "doc.text.fill")
                                .font(.system(size: 11))
                                .foregroundColor(.accentColor)
                            
                            Text("active_lab.py")
                                .font(.system(size: 10, weight: .bold, design: .monospaced))
                                .foregroundColor(.secondary)
                            
                            Spacer()
                            
                            Button(action: resetCode) {
                                HStack(spacing: 4) {
                                    Image(systemName: "arrow.counterclockwise")
                                    Text("Reset")
                                }
                                .font(.system(size: 10, weight: .bold, design: .monospaced))
                                .padding(.vertical, 4)
                                .padding(.horizontal, 8)
                                .background(isResetHovered ? Color.primary.opacity(0.05) : Color.clear)
                                .cornerRadius(4)
                            }
                            .buttonStyle(PlainButtonStyle())
                            .disabled(viewModel.activeContent == nil)
                            .onHover { hovering in
                                self.isResetHovered = hovering
                            }
                            .scaleEffect(isResetHovered ? 1.02 : 1.0)
                            .animation(.spring(response: 0.2, dampingFraction: 0.6), value: isResetHovered)
                            
                            Button(action: verifyCode) {
                                HStack(spacing: 6) {
                                    if viewModel.isRunningTests {
                                        ProgressView()
                                            .scaleEffect(0.4)
                                    } else {
                                        Image(systemName: "play.fill")
                                    }
                                    Text("Verify Code")
                                }
                                .font(.system(size: 10, weight: .bold, design: .monospaced))
                                .foregroundColor(.white)
                                .padding(.vertical, 5)
                                .padding(.horizontal, 12)
                                .background(
                                    viewModel.isRunningTests 
                                    ? Color.gray 
                                    : (isVerifyHovered ? Color.accentColor.opacity(0.9) : Color.accentColor)
                                )
                                .cornerRadius(5)
                                .shadow(color: isVerifyHovered ? Color.accentColor.opacity(0.25) : .clear, radius: 4, x: 0, y: 2)
                            }
                            .buttonStyle(PlainButtonStyle())
                            .disabled(viewModel.activeContent == nil || viewModel.isRunningTests)
                            .onHover { hovering in
                                self.isVerifyHovered = hovering
                            }
                            .scaleEffect(isVerifyHovered ? 1.03 : 1.0)
                            .animation(.spring(response: 0.2, dampingFraction: 0.6), value: isVerifyHovered)
                        }
                        .padding(.horizontal, 16)
                        .frame(height: 38)
                        .background(Color.black.opacity(0.02))
                        
                        Divider()
                            .background(Color.primary.opacity(0.05))
                        
                        // Code Editor Pane - standard translucent editor background
                        TextEditor(text: $viewModel.activeCode)
                            .font(.system(.body, design: .monospaced))
                            .padding(10)
                            .background(Color.clear) // Full translucency seeps through
                    }
                    .background(.thinMaterial)
                    .cornerRadius(12)
                    .overlay(
                        RoundedRectangle(cornerRadius: 12)
                            .stroke(Color.primary.opacity(0.08), lineWidth: 1)
                    )
                    .shadow(color: Color.black.opacity(0.02), radius: 6, x: 0, y: 3)
                    
                    // High-Density Bento Terminal Console - Glassmorphic terminal
                    if !consoleOutput.isEmpty {
                        VStack(spacing: 0) {
                            HStack {
                                Image(systemName: "terminal.fill")
                                    .font(.system(size: 10))
                                    .foregroundColor(.green)
                                
                                Text("Console Logs")
                                    .font(.system(size: 10, weight: .bold, design: .monospaced))
                                    .foregroundColor(.secondary)
                                Spacer()
                                Button("Clear") {
                                    consoleOutput = ""
                                }
                                .font(.system(size: 10, weight: .bold, design: .monospaced))
                                .foregroundColor(.secondary)
                                .buttonStyle(PlainButtonStyle())
                            }
                            .padding(.horizontal, 16)
                            .frame(height: 32)
                            .background(Color.black.opacity(0.2))
                            
                            Divider()
                                .background(Color.white.opacity(0.05))
                            
                            ScrollView {
                                Text(consoleOutput)
                                    .font(.system(.caption, design: .monospaced))
                                    .foregroundColor(.green)
                                    .frame(maxWidth: .infinity, alignment: .leading)
                                    .padding(12)
                            }
                            .frame(height: 120)
                            .background(Color.black.opacity(0.4)) // Semi-transparent terminal backing
                        }
                        .cornerRadius(12)
                        .overlay(
                            RoundedRectangle(cornerRadius: 12)
                                .stroke(Color.primary.opacity(0.08), lineWidth: 1)
                        )
                        .transition(.move(edge: .bottom).combined(with: .opacity))
                        .animation(.spring(response: 0.3, dampingFraction: 0.7), value: consoleOutput)
                    }
                }
                .padding(.top, 8)
                .padding(.horizontal, 16)
                .padding(.bottom, 16)
            }
            .frame(minHeight: 280)
        }
    }
    
    func resetCode() {
        if let content = viewModel.activeContent, let first = content.exercises.first {
            viewModel.activeCode = first.starter_code
        }
    }
    
    func verifyCode() {
        guard let content = viewModel.activeContent else { return }
        
        consoleOutput = "Spawning isolated Python verification subprocess...\n\n"
        viewModel.isRunningTests = true
        
        // Grab assertions for the active exercise
        let assertions = content.exercises.map { $0.assertions }.joined(separator: "\n")
        
        // Use persistent viewModel.executor instead of a localized struct member
        viewModel.executor.execute(
            code: viewModel.activeCode,
            assertions: assertions,
            onOutput: { output in
                // Safely update console text on @MainActor
                DispatchQueue.main.async {
                    self.consoleOutput += output
                }
            },
            onCompletion: { success in
                // Safely update state on @MainActor
                DispatchQueue.main.async {
                    viewModel.isRunningTests = false
                    if success {
                        self.consoleOutput += "\n\n[SUCCESS] All assertions passed successfully! Playbook solved."
                        
                        if let selected = viewModel.selectedLesson {
                            Task {
                                await trackProgress(lessonId: selected.id)
                            }
                        }
                    } else {
                        self.consoleOutput += "\n\n[FAILURE] Code verification failed. Ask Carl for Socratic guidance."
                    }
                }
            }
        )
    }
    
    func trackProgress(lessonId: String) async {
        guard let url = URL(string: "http://127.0.0.1:5050/api/track") else { return }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let payload: [String: String] = ["lesson": lessonId]
        request.httpBody = try? JSONEncoder().encode(payload)
        
        _ = try? await URLSession.shared.data(for: request)
    }
}

// MARK: - Bespoke Bento Panel Container Component (Liquid Glass)
struct BentoPanel<Content: View>: View {
    let title: String
    let systemIcon: String
    let content: Content
    
    init(title: String, systemIcon: String, @ViewBuilder content: () -> Content) {
        self.title = title
        self.systemIcon = systemIcon
        self.content = content()
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Card Header
            HStack(spacing: 8) {
                Image(systemName: systemIcon)
                    .font(.system(size: 11, weight: .bold))
                    .foregroundColor(.accentColor)
                
                Text(title.uppercased())
                    .font(.system(size: 10, weight: .bold, design: .monospaced))
                    .foregroundColor(.secondary)
                
                Spacer()
            }
            .padding(.horizontal, 16)
            .frame(height: 34)
            .background(Color.black.opacity(0.01))
            
            Divider()
                .background(Color.primary.opacity(0.05))
            
            // Card Content
            content
                .frame(maxHeight: .infinity)
        }
        .background(.thinMaterial)
        .cornerRadius(12)
        .overlay(
            RoundedRectangle(cornerRadius: 12)
                .stroke(Color.primary.opacity(0.08), lineWidth: 1)
        )
        .shadow(color: Color.black.opacity(0.02), radius: 6, x: 0, y: 3)
    }
}
