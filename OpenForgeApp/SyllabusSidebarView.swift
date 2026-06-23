import SwiftUI

struct SyllabusSidebarView: View {
    @ObservedObject var viewModel: SyllabusViewModel
    
    var body: some View {
        VStack(spacing: 0) {
            // Elegant, custom-designed Sidebar Header
            HStack {
                Text("SYLLABUS MAP")
                    .font(.system(size: 10, weight: .bold, design: .monospaced))
                    .foregroundColor(viewModel.activeTheme == .warpDark || viewModel.activeTheme == .warpCarbon ? .white.opacity(0.6) : Color(red: 0.31, green: 0.38, blue: 0.48))
                Spacer()
            }
            .padding(.horizontal, 24)
            .frame(height: 52)
            
            Divider()
                .background(Color.primary.opacity(0.05))
            
            // Custom, fully scrollable navigation tree
            ScrollView {
                VStack(alignment: .leading, spacing: 6) {
                    ForEach(viewModel.lessons) { lesson in
                        SidebarRow(
                            title: lesson.title,
                            icon: "terminal.fill",
                            isSelected: viewModel.selectedLesson == lesson,
                            activeTheme: viewModel.activeTheme
                        ) {
                            viewModel.selectLesson(lesson)
                        }
                    }
                }
                .padding(.vertical, 16)
                .padding(.horizontal, 12)
            }
        }
        .overlay(
            GeometryReader { geo in
                HStack {
                    Spacer()
                    Rectangle()
                        .fill(Color.primary.opacity(0.05))
                        .frame(width: 1)
                        .frame(maxHeight: .infinity)
                }
            }
        )
    }
}

// MARK: - Bespoke, Spring-Animated Navigation Node
struct SidebarRow: View {
    let title: String
    let icon: String
    let isSelected: Bool
    let activeTheme: AppTheme
    let action: () -> Void
    
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            HStack(spacing: 12) {
                Image(systemName: icon)
                    .font(.system(size: 12, weight: .semibold))
                    .foregroundColor(isSelected ? activeTheme.accentColor : activeTheme.textColor.opacity(0.6))
                    .frame(width: 16, height: 16)
                
                Text(title)
                    .font(.system(size: 13, weight: isSelected ? .semibold : .regular))
                    .foregroundColor(isSelected ? activeTheme.accentColor : activeTheme.textColor)
                    .lineLimit(1)
                    .truncationMode(.tail)
                
                Spacer()
            }
            .padding(.vertical, 8)
            .padding(.horizontal, 12)
            .background(
                isSelected 
                ? activeTheme.accentColor.opacity(0.08)
                : (isHovered ? Color.primary.opacity(0.05) : Color.clear)
            )
            .cornerRadius(8)
            .overlay(
                RoundedRectangle(cornerRadius: 8)
                    .stroke(isSelected ? activeTheme.accentColor.opacity(0.2) : Color.clear, lineWidth: 1)
            )
            .scaleEffect(isHovered ? 1.015 : 1.0)
            .animation(.spring(response: 0.22, dampingFraction: 0.65), value: isHovered)
            .animation(.easeIn(duration: 0.12), value: isSelected)
        }
        .buttonStyle(PlainButtonStyle())
        .onHover { hovering in
            self.isHovered = hovering
        }
    }
}
