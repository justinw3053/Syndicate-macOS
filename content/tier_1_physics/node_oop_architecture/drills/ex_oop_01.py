# PROBLEM: Class Initialization and attributes
#
# Instance attributes are defined inside the `__init__` constructor using `self`.
#
# Your Task: Complete the PromptSegment class to store 'content' and 'role'.

class PromptSegment:
    def __init__(self, content: str, role: str):
        # Step 1: Assign content and role instance attributes
        self.content = content
        self.role = role
        
    def to_dict(self) -> dict:
        # Step 2: Return content and role mapped in a dictionary
        return {"content": self.content, "role": self.role}
