# Textbook: Reading Files Securely (KATA_FILE_01)

## Theoretical Foundation
To build a RAG (Retrieval-Augmented Generation) system, we must read documents from disk. Using the `with open(...)` context manager is a core programming standard. It safeguards your OS from file descriptor leaks and memory leaks by ensuring the file handles are released unconditionally.

---

## Syntax Anatomy
```python
with open("doc.txt", "r", encoding="utf-8") as f:
  text = f.read()
```

---

## Step-by-Step Exercise Instructions
1. Open `file_path` inside a `with open(file_path, "r", encoding="utf-8") as f:` block.
2. Read the full text using `f.read()`.
3. Return the string content.
