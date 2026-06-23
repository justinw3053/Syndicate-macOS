# Textbook: Trimming & Padding Text (KATA_STR_01)

## Theoretical Foundation
Data sanitization is the first step in any NLP or GenAI parsing pipeline. Raw prompts, scraping outputs, or user inputs arrive littered with leading tabs, trailing spaces, or carriage returns. If left uncleaned, these characters will pollute tokenizer splits and skew vocabulary indices. 

We use `.strip()` to cleanly purge whitespaces, and `.rjust()`/`.ljust()` to pad text, ensuring aligned data spacing in telemetry logs or tabular outputs.

---

## Syntax Anatomy
```python
text = " hello "
cleaned = text.strip() # "hello"
padded = cleaned.rjust(10, "-") # "-----hello"
```

---

## Step-by-Step Exercise Instructions
1. Call `.strip()` on `raw_text` to eliminate surrounding whitespace.
2. Call `.rjust(10, "-")` on the trimmed text to pad it to a width of 10.
3. Return the result.
