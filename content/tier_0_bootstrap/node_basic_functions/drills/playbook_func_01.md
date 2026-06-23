# Textbook: Introduction to Dictionaries (KATA_FUNC_01)

## Theoretical Foundation
A dictionary stores key-value associations inside curly braces `{}`. It maps a unique lookup label (the key) to its associated value. We look up elements using bracket notation:
```python
config = {"model": "qwen"}
model_name = config["model"] # Returns "qwen"
```

---

## Step-by-Step Exercise Instructions
1. Locate `get_model_name(config)`.
2. Look up the key `"model"` inside `config` and assign it to a new variable named `model_name`.
3. Return `model_name`.
