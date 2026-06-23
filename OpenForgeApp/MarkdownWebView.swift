import SwiftUI
import WebKit

struct MarkdownWebView: View {
    let markdown: String
    
    var body: some View {
        WebViewRepresentable(markdown: markdown)
    }
}

struct WebViewRepresentable: NSViewRepresentable {
    let markdown: String
    
    func makeNSView(context: Context) -> WKWebView {
        let webView = WKWebView()
        // Ensure transparent background to let the translucent material seep through
        webView.setValue(false, forKey: "drawsBackground")
        return webView
    }
    
    func updateNSView(_ nsView: WKWebView, context: Context) {
        // Escape special characters to prevent JavaScript template literal crashes
        let escapedMarkdown = markdown
            .replacingOccurrences(of: "\\", with: "\\\\")
            .replacingOccurrences(of: "`", with: "\\`")
            .replacingOccurrences(of: "$", with: "\\$")
        
        let html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                /* DEFAULT LIGHT MODE STYLING */
                body {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    font-size: 13.5px;
                    line-height: 1.6;
                    color: #1E293B; /* Slate 800 (Dark Charcoal) */
                    background-color: transparent;
                    padding: 8px;
                }
                pre {
                    background-color: #F8FAFC; /* Slate 50 */
                    padding: 12px;
                    border-radius: 6px;
                    border: 1px solid #E2E8F0;
                    overflow-x: auto;
                }
                code {
                    font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
                    background-color: #F1F5F9; /* Slate 100 */
                    padding: 2px 4px;
                    border-radius: 4px;
                    font-size: 11.5px;
                    color: #0F172A;
                }
                pre code {
                    background-color: transparent;
                    padding: 0;
                    border-radius: 0;
                    border: none;
                }
                h1, h2, h3 {
                    color: #4F46E5; /* Solid Indigo 600 */
                    font-weight: 600;
                    margin-top: 1.5em;
                }
                h1:first-child, h2:first-child, h3:first-child {
                    margin-top: 0;
                }
                a {
                    color: #4F46E5;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                p {
                    margin-bottom: 1em;
                }
                ul, ol {
                    padding-left: 20px;
                    margin-bottom: 1em;
                }
                li {
                    margin-bottom: 0.5em;
                }
                
                /* DYNAMIC DARK MODE STYLING (Auto-applied by OS) */
                @media (prefers-color-scheme: dark) {
                    body {
                        color: #F1F5F9; /* Slate 50 (Glow Off-White) - Perfect Contrast */
                    }
                    pre {
                        background-color: #1E293B; /* Slate 800 (Deep Charcoal) */
                        border-color: #334155; /* Slate 700 */
                    }
                    code {
                        background-color: #334155; /* Slate 700 */
                        color: #F8FAFC; /* Slate 50 */
                    }
                    h1, h2, h3 {
                        color: #818CF8; /* Light Indigo 400 - Vibrant highlight in dark mode */
                    }
                    a {
                        color: #818CF8;
                    }
                }
            </style>
            <script>
            window.MathJax = {
              tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
              },
              options: {
                ignoreHtmlClass: 'tex2jax_ignore',
                processHtmlClass: 'tex2jax_process'
              }
            };
            </script>
            <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
            <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        </head>
        <body class="tex2jax_process">
            <div id="content"></div>
            <script>
                try {
                    var rawMarkdown = `\(escapedMarkdown)`;
                    document.getElementById('content').innerHTML = marked.parse(rawMarkdown);
                    
                    // Trigger MathJax typesetting asynchronously to render equations
                    if (window.MathJax && window.MathJax.typeset) {
                        window.MathJax.typeset();
                    } else {
                        document.addEventListener("DOMContentLoaded", function() {
                            if (window.MathJax && window.MathJax.typeset) {
                                window.MathJax.typeset();
                            }
                        });
                    }
                } catch (e) {
                    document.getElementById('content').innerText = "Rendering error: " + e.message;
                }
            </script>
        </body>
        </html>
        """
        
        nsView.loadHTMLString(html, baseURL: nil)
    }
}
