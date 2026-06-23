# PROBLEM: Simple State Transition
# A state machine moves from one state to another based on rules.
#
# Your Task: Implement transition(current_state: str, event: str) -> str
# States: "idle", "processing", "error"
# Rules: 
# - idle + "start" -> "processing"
# - processing + "fail" -> "error"
# - processing + "finish" -> "idle"
# - Any other combination returns the current_state unchanged.

def transition(current_state: str, event: str) -> str:
    # STUDENT_IMPLEMENTATION: Implement state transition rules
    pass
