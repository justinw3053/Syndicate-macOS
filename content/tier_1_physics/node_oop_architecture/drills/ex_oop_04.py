# PROBLEM: Direct Equality Check Override (__eq__)
#
# Overriding __eq__ checks structural property equality rather than pointer identity (is).
#
# Your Task: Complete the class to assert equality if 'uuid' matches, regardless of pointer memory address.

class AgentState:
    def __init__(self, uuid: str, name: str):
        self.uuid = uuid
        self.name = name
        
    def __eq__(self, other) -> bool:
        # Step 1: Check if other is an instance of AgentState
        if not isinstance(other, AgentState):
            return False
        # Step 2: Assert equality based on self.uuid and other.uuid
        return self.uuid == other.uuid
