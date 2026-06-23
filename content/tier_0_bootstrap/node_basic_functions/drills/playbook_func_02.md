# Textbook: Safe Dictionary Lookups - .get (KATA_FUNC_02)

## Theoretical Foundation
Attempting to fetch a key that doesn't exist using standard brackets causes a fatal `KeyError` crash. To build resilient applications, we use the `.get()` method. It accepts a target key, and a default fallback value to return if the key is missing.

Example:
```python
val = config.get("missing_key", "default_val")
```

---

## Step-by-Step Exercise Instructions
1. Safely extract `"temperature"` from `config` using `.get("temperature", 0.7)`.
2. Return the retrieved temperature.
