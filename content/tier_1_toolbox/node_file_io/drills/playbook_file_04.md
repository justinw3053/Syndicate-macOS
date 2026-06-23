# Textbook: Deserializing JSON payloads (KATA_FILE_04)

## Theoretical Foundation
When we fetch model outputs or query an API, the server responds with raw text formatted as JSON. **Deserialization** decodes this text string back into an active Python dictionary, unlocking key-value lookup.

---

## Step-by-Step Exercise Instructions
1. Parse the `json_data` string using `json.loads(json_data)`.
2. Return the parsed dictionary.
