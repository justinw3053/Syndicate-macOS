"""
Kata: Context Guard Flags & State Transitions
Objective: Evaluate whether an agent's current context allows it to transition 
from one state node to another based on pre/post conditions.
"""

# STUDENT_IMPLEMENTATION 1:
# Evaluate a boolean guard flag against the current status of an agent.
# If 'guard' is True and the 'status' matches, return True (allow transition).
def evaluate_guard(guard: bool, expected_status: str, current_status: str) -> bool:
      pass


# STUDENT_IMPLEMENTATION 2:
# Given a list of state objects (each containing a 'flag' key),
# filter out states where the flag is strictly False.
def filter_active_flags(states: list[dict]) -> list[dict]:
    return []


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Simulate a guarded transition! Check if we can move from 'initial_state' 
# to 'target_state' ONLY IF the node's guard flag is True.
def enforce_transition(flags_map: dict[str, bool], initial: str, target: str) -> bool:
     guard = flags_map.get(initial, False)
    pass
