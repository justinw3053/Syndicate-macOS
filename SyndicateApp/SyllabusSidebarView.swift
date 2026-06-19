import SwiftUI

struct SyllabusSidebarView: View {
    @ObservedObject var viewModel: SyllabusViewModel
    
    var prepLessons: [Lesson] {
        viewModel.lessons.filter { $0.id.contains("phase_0_prep") }
    }
    
    var coreLessons: [Lesson] {
        viewModel.lessons.filter { !$0.id.contains("phase_0_prep") }
    }
    
    var body: some View {
        VStack(spacing: 0) {
            // Elegant, minimalist Sidebar Header
            HStack {
                Text("SYNDICATE PLAYBOOKS")
                    .font(.system(size: 10, weight: .bold, design: .monospaced))
                    .foregroundColor(.secondary.opacity(0.8))
                Spacer()
            }
            .padding(.horizontal, 24)
            .frame(height: 52)
            
            Divider()
                .background(Color.primary.opacity(0.05))
            
            // Custom, fully scrollable navigation tree (bypasses default List styling)
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    
                    // Section 1: Prep Phase
                    VStack(alignment: .leading, spacing: 6) {
                        Text("Prep Phase (Phase 0)")
                            .font(.system(size: 10, weight: .bold))
                            .foregroundColor(.secondary.opacity(0.8))
                            .padding(.horizontal, 12)
                            .padding(.bottom, 2)
                        
                        ForEach(prepLessons) { lesson in
                            SidebarRow(
                                title: lesson.title,
                                icon: "graduationcap.fill",
                                isSelected: viewModel.selectedLesson == lesson
                            ) {
                                viewModel.selectLesson(lesson)
                            }
                        }
                    }
                    
                    // Section 2: Core Curriculum
                    VStack(alignment: .leading, spacing: 6) {
                        Text("Core Milestones")
                            .font(.system(size: 10, weight: .bold))
                            .foregroundColor(.secondary.opacity(0.8))
                            .padding(.horizontal, 12)
                            .padding(.bottom, 2)
                        
                        ForEach(coreLessons) { lesson in
                            let isFinal = lesson.id.contains("phase_10")
                            let isBrain = lesson.id.contains("phase_8") || lesson.id.contains("phase_9")
                            SidebarRow(
                                title: lesson.title,
                                icon: isFinal ? "crown.fill" : (isBrain ? "brain" : "cpu.fill"),
                                isSelected: viewModel.selectedLesson == lesson
                            ) {
                                viewModel.selectLesson(lesson)
                            }
                        }
                    }
                }
                .padding(.vertical, 16)
                .padding(.horizontal, 12)
            }
        }
        .frame(minWidth: 260, maxWidth: 340)
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
    let action: () -> Void
    
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            HStack(spacing: 12) {
                Image(systemName: icon)
                    .font(.system(size: 12, weight: .semibold))
                    .foregroundColor(isSelected ? .accentColor : .secondary.opacity(0.7))
                    .frame(width: 16, height: 16)
                
                Text(title)
                    .font(.system(size: 13, weight: isSelected ? .semibold : .regular))
                    .foregroundColor(isSelected ? .primary : .primary.opacity(0.8))
                    .lineLimit(1)
                    .truncationMode(.tail)
                
                Spacer()
            }
            .padding(.vertical, 8)
            .padding(.horizontal, 12)
            .background(
                isSelected 
                ? Color.accentColor.opacity(0.12)
                : (isHovered ? Color.primary.opacity(0.05) : Color.clear)
            )
            .cornerRadius(8)
            .overlay(
                RoundedRectangle(cornerRadius: 8)
                    .stroke(isSelected ? Color.accentColor.opacity(0.25) : Color.clear, lineWidth: 1)
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
