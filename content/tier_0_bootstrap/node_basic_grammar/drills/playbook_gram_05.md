# Textbook: Extracting Items - List Indexing (KATA_GRAM_05)

## Theoretical Foundation
To retrieve a single item from a list, we use its position index inside brackets. In computer programming, we always start counting positions at **ZERO (0)**, not 1!
*   Index 0 is the first item.
*   Index 1 is the second item.
*   Index 2 is the third item, and so on.

Example:
```python
colors = ["red", "green", "blue"]
first_color = colors[0]   # This extracts "red"
```

---

## Syntax Anatomy
```python
def get_first_item(tokens):
    first_token = tokens[0]
    return first_token
```

---

## Step-by-Step Exercise Instructions
1. Locate the `get_first_item(tokens)` function.
2. Inside the function, extract the very first item from the list `tokens` (which is at index 0) and assign it to a new variable named `first_token`.
3. Return `first_token`.
