import SwiftUI

struct AnsiText: View {
    let text: String
    
    var body: some View {
        parseAnsi(text)
            .font(.system(size: 11, weight: .medium, design: .monospaced))
            .lineSpacing(4)
            .frame(maxWidth: .infinity, alignment: .leading)
    }
    
    /// Parses ANSI escape codes (e.g. \u{001B}[32m) and compiles them into concatenated, colorized SwiftUI Text runs
    private func parseAnsi(_ input: String) -> Text {
        var result = Text("")
        let parts = input.components(separatedBy: "\u{001B}[")
        
        for (index, part) in parts.enumerated() {
            if index == 0 {
                result = Text("\(result)\(Text(part))")
                continue
            }
            
            // Find the closing 'm' of the ANSI sequence
            guard let mIndex = part.firstIndex(of: "m") else {
                result = Text("\(result)\(Text("\u{001B}[\(part)"))")
                continue
            }
            
            let command = String(part[..<mIndex])
            let content = String(part[part.index(after: mIndex)...])
            
            var textRun = Text(content)
            
            // Parse individual code segments separated by semicolons (e.g., "1;31")
            let codes = command.components(separatedBy: ";")
            for code in codes {
                switch code {
                case "0": // Reset
                    textRun = textRun.foregroundColor(.primary).font(.system(size: 11, weight: .medium, design: .monospaced))
                case "1": // Bold
                    textRun = textRun.bold()
                case "31", "91": // Red / Bright Red
                    textRun = textRun.foregroundColor(.red)
                case "32", "92": // Green / Bright Green
                    textRun = textRun.foregroundColor(.green)
                case "33", "93": // Yellow / Bright Yellow
                    textRun = textRun.foregroundColor(.orange)
                case "34", "94": // Blue / Bright Blue
                    textRun = textRun.foregroundColor(.blue)
                case "35", "95": // Magenta / Bright Magenta
                    textRun = textRun.foregroundColor(.purple)
                case "36", "96": // Cyan / Bright Cyan
                    textRun = textRun.foregroundColor(.cyan)
                case "37": // White / Subdued
                    textRun = textRun.foregroundColor(.primary)
                default:
                    break
                }
            }
            
            result = Text("\(result)\(textRun)")
        }
        
        return result
    }
}
