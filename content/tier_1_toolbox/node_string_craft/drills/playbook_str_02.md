# Textbook: Splitting Text by Delimiters (KATA_STR_02)

## Theoretical Foundation
Raw log telemetry or prompt structures pack multiple attributes into single strings using delimiter characters (like `|`, `,`, or `:`). Splitting these strings using `.split()` transforms structured strings into arrays, enabling parsing and remapping loops.

---

## Syntax Anatomy
```python
log_line = "metric:0.95|status:active"
parts = log_line.split("|") # ["metric:0.95", "status:active"]
```

---

## Step-by-Step Exercise Instructions
1. Call `raw_data.split("|")` to split the string by the pipe delimiter.
2. Return the resulting list.
