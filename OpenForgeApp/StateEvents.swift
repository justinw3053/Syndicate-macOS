import Foundation

// Unidirectional Data Flow (UDF) Actions
enum StateAction: Codable, Hashable {
    case lessonCompleted(lessonId: String)
    case themeChanged(themeName: String)
    // Future Expansion:
    // case chatCleared
    // case modelChanged(modelName: String)
}

struct StateEvent: Codable {
    let type: String
    let action: StateAction
    let timestamp: Date
}
