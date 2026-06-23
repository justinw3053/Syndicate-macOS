# PROBLEM: Custom Representation Hook (__repr__)
#
# Overriding __repr__ outputs professional developer-friendly logs in debugging.
#
# Your Task: Complete the class so that `repr(token)` returns `"Token(value='word', id=42)"`.

class Token:
    def __init__(self, value: str, token_id: int):
        self.value = value
        self.token_id = token_id
        
    def __repr__(self) -> str:
        # Step 1: Construct the custom developer repr representation string
        return f"Token(value={repr(self.value)}, id={self.token_id})"
