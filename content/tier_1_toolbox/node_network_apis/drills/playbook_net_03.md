# Textbook: HTTP Response Status Validation (KATA_NET_03)

## Theoretical Foundation
Robust systems validate response codes before parsing content. If a server returns an error (like `403 Forbidden` or `500 Server Error`), attempting to parse the result as standard JSON will crash your app. Python's `urllib` raises an `HTTPError` for any code $\ge 400$, which we must catch to read the error code.

---

## Step-by-Step Exercise Instructions
1. Wrap the request inside a `try-except urllib.error.HTTPError:` block.
2. In the `try` block, open the URL and return `response.status`.
3. In the `except` block, catch `urllib.error.HTTPError as e` and return `e.code`.
