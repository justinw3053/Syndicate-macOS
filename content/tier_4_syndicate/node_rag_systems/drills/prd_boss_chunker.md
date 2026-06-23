# PRD: Token-Overlapping Chunker
Implement `chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]`.
1. Split the string by spaces into a list of words.
2. Yield chunks of `chunk_size` words.
3. Each subsequent chunk must overlap with the previous chunk by `overlap` words.
