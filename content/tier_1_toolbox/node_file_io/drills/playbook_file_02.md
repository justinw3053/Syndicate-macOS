# Textbook: Writing Files Securely (KATA_FILE_02)

## Theoretical Foundation
Logging telemetry, recording agent trajectories, or saving chat histories requires writing local text files. Write mode `"w"` overwrites any existing file content at the path.

---

## Step-by-Step Exercise Instructions
1. Open `file_path` inside a `with open(file_path, "w", encoding="utf-8") as f:` block.
2. Write the log string using `f.write(telemetry_log)`.
