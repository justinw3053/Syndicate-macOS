# PRD: The Enforced Buffer
Create a `PromptBuffer` class from scratch.
- It should store an internal list of strings.
- Implement `__len__` so calling `len(buffer)` returns the count of items.
- Implement a custom `append(text: str)` method that raises a `TypeError` if the appended item is not a string.
