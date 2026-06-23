# Textbook: API Connection Timeouts (KATA_NET_04)

## Theoretical Foundation
Autoregressive LLM generation can hang if servers are overloaded. To keep your local desktop application snappy and responsive, you must always enforce socket timeouts. This prevents thread hangs and gives immediate feedback.

---

## Step-by-Step Exercise Instructions
1. Set up a `try` block.
2. Open the URL using `urllib.request.urlopen(url, timeout=timeout_seconds)`.
3. Catch any `socket.timeout` or `urllib.error.URLError` exception.
4. Return `"timeout_exceeded"` on failure.
