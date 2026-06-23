# Textbook: Portable Path Joining (KATA_FILE_05)

## Theoretical Foundation
If you join files using static string formatting (like `f"{folder}/{file}"`), your app will immediately fail on Windows systems. We must write platform-agnostic, portable paths using the standard `os.path` library.

---

## Syntax Anatomy
```python
import os
full_path = os.path.join("documents", "RAG", "db")
if not os.path.exists(full_path):
  os.makedirs(full_path)
```

---

## Step-by-Step Exercise Instructions
1. Use `os.path.exists(base_dir)` to check if the directory exists.
2. If it is missing, create it using `os.makedirs(base_dir)`.
3. Combine the path using `os.path.join(base_dir, filename)` and return it.
