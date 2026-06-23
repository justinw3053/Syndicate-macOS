# Textbook: Serializing to JSON Strings (KATA_FILE_03)

## Theoretical Foundation
Dictionaries exist in memory, but external APIs and text logs only understand text strings. **Serialization** (marshalling) encodes key-value memory blocks into standardized JSON text lines, allowing seamless network communication.

---

## Step-by-Step Exercise Instructions
1. Import `json`.
2. Convert the `data` dictionary using `json.dumps(data)`.
3. Return the serialized JSON string.
