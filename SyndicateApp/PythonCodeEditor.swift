import SwiftUI
import AppKit

// MARK: - High-Performance Python Syntax Highlighter
class PythonSyntaxHighlighter {
    var keywordColor = NSColor.systemIndigo
    var stringColor = NSColor.systemGreen
    var commentColor = NSColor.systemGray
    var numberColor = NSColor.systemOrange
    var defaultColor = NSColor.textColor
    
    func highlight(attributedString: NSMutableAttributedString) {
        let range = NSRange(location: 0, length: attributedString.length)
        
        // Reset to default style first
        attributedString.addAttribute(.foregroundColor, value: defaultColor, range: range)
        attributedString.addAttribute(.font, value: NSFont.monospacedSystemFont(ofSize: 12, weight: .medium), range: range)
        
        // 1. Highlight Keywords: def, class, return, import, from, if, else, elif, for, in, while, try, except, as, with, pass, True, False, None
        let keywordPattern = "\\b(def|class|return|import|from|if|else|elif|for|in|while|try|except|as|with|pass|True|False|None)\\b"
        applyRegex(pattern: keywordPattern, color: keywordColor, in: attributedString)
        
        // 2. Highlight Numbers
        let numberPattern = "\\b(\\d+)\\b"
        applyRegex(pattern: numberPattern, color: numberColor, in: attributedString)
        
        // 3. Highlight Strings (Single and double quotes, multiline docstrings)
        let stringPattern = "(\"\"\"[\\s\\S]*?\"\"\"|'''[\\s\\S]*?'''|\"[^\"]*\"|'[^']*')"
        applyRegex(pattern: stringPattern, color: stringColor, in: attributedString)
        
        // 4. Highlight Comments
        let commentPattern = "(#.*)"
        applyRegex(pattern: commentPattern, color: commentColor, in: attributedString)
    }
    
    private func applyRegex(pattern: String, color: NSColor, in attributedString: NSMutableAttributedString) {
        guard let regex = try? NSRegularExpression(pattern: pattern, options: []) else { return }
        let matches = regex.matches(in: attributedString.string, options: [], range: NSRange(location: 0, length: attributedString.length))
        for match in matches {
            attributedString.addAttribute(.foregroundColor, value: color, range: match.range)
        }
    }
}

// MARK: - Native AppKit-based Highlighting Code Editor View
struct PythonCodeEditor: NSViewRepresentable {
    @Binding var text: String
    var activeTheme: AppTheme
    
    func makeNSView(context: Context) -> NSScrollView {
        let scrollView = NSTextView.scrollableTextView()
        let textView = scrollView.documentView as! NSTextView
        
        textView.font = NSFont.monospacedSystemFont(ofSize: 12.5, weight: .medium)
        textView.isAutomaticQuoteSubstitutionEnabled = false
        textView.isAutomaticDashSubstitutionEnabled = false
        textView.isAutomaticTextReplacementEnabled = false
        textView.isAutomaticSpellingCorrectionEnabled = false
        textView.isAutomaticLinkDetectionEnabled = false
        textView.isRichText = false
        textView.delegate = context.coordinator
        
        // Allow the scroll container to be completely transparent
        scrollView.drawsBackground = false
        textView.drawsBackground = true
        
        return scrollView
    }
    
    func updateNSView(_ nsView: NSScrollView, context: Context) {
        let textView = nsView.documentView as! NSTextView
        
        // Live theme color mappings
        context.coordinator.updateTheme(activeTheme, textView: textView)
        
        if textView.string != text {
            textView.string = text
            context.coordinator.highlight(textView: textView)
        }
    }
    
    func makeCoordinator() -> Coordinator {
        Coordinator(text: $text)
    }
    
    class Coordinator: NSObject, NSTextViewDelegate {
        @Binding var text: String
        let highlighter = PythonSyntaxHighlighter()
        private var isHighlighting = false
        
        init(text: Binding<String>) {
            self._text = text
        }
        
        func textDidChange(_ notification: Notification) {
            guard let textView = notification.object as? NSTextView else { return }
            self.text = textView.string
            highlight(textView: textView)
        }
        
        func updateTheme(_ theme: AppTheme, textView: NSTextView) {
            highlighter.keywordColor = NSColor(theme.accentColor)
            
            if theme == .warpDark || theme == .warpCarbon {
                highlighter.stringColor = NSColor.systemGreen
                highlighter.commentColor = NSColor.textColor.withAlphaComponent(0.4)
                highlighter.numberColor = NSColor.systemOrange
                highlighter.defaultColor = NSColor.white
                
                textView.backgroundColor = NSColor(theme.textEditorBackground)
                textView.textColor = NSColor.white
            } else {
                // Editorial Light / Liquid Glass mapping
                highlighter.stringColor = NSColor(red: 0.1, green: 0.52, blue: 0.22, alpha: 1.0)
                highlighter.commentColor = NSColor.textColor.withAlphaComponent(0.4)
                highlighter.numberColor = NSColor.systemOrange
                
                if theme == .systemGlass {
                    highlighter.defaultColor = NSColor.textColor
                    textView.backgroundColor = NSColor.clear
                    textView.textColor = NSColor.textColor
                } else {
                    highlighter.defaultColor = NSColor(theme.textColor)
                    textView.backgroundColor = NSColor(theme.textEditorBackground)
                    textView.textColor = NSColor(theme.textColor)
                }
            }
            
            // Make insertion caret match active theme accent color (glowing cyan, orange, indigo)
            textView.insertionPointColor = NSColor(theme.accentColor)
        }
        
        func highlight(textView: NSTextView) {
            guard !isHighlighting else { return }
            isHighlighting = true
            
            let textStorage = textView.textStorage
            let selectedRange = textView.selectedRange()
            
            textStorage?.beginEditing()
            highlighter.highlight(attributedString: textStorage!)
            textStorage?.endEditing()
            
            textView.setSelectedRange(selectedRange)
            isHighlighting = false
        }
    }
}
