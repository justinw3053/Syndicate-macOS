# Textbook: HTTP GET Requests (KATA_NET_01)

## Theoretical Foundation
An agent cannot act in isolation; it must connect to external servers, APIs, and microservices. Python's standard `urllib.request` library lets you query web resources natively without requiring heavy external dependencies (like `requests` or `aiohttp`), ensuring lightweight execution in sandboxed desktop applications.

---

## Syntax Anatomy
```python
import urllib.request
with urllib.request.urlopen("https://api.ollama.com") as resp:
  data = resp.read().decode("utf-8")
```

---

## Step-by-Step Exercise Instructions
1. Import `urllib.request`.
2. Wrap `urllib.request.urlopen(url)` inside a `with` block.
3. Read the payload bytes (`response.read()`) and decode to UTF-8 (`.decode("utf-8")`).
4. Return the decoded string.
