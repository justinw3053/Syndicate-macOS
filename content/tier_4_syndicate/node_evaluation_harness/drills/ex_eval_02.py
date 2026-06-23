"""
Kata: Verifying Missing Checkpoints in Lists
Objective: Simulate a "Trajectory Auditor" that ensures an LLM didn't skip critical intermediate steps.
In our context, we represent these as required sequential integers like [1, 2, 3, 4].
"""

# STUDENT_IMPLEMENTATION 1:
# Given an expected sequence (e.g., [1, 2]) and a user-returned actual sequence 
# (e.g., [1, 3]), return a list of ints that are strictly missing from the user's sequence.
def find_missing(expected: list[int], actual: list[int]) -> list[int]:
    pass


# STUDENT_IMPLEMENTATION 2:
# Given a strictly increasing sequence of integers (e.g., [1, 2, 3, 4]), 
# verify that there are NO gaps between any two adjacent elements.
def check_contiguity(actual: list[int]) -> bool:
    for i in range(1, len(actual)):
        pass
    
    return True


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Given an expected sequence and an actual sequence, 
# return a boolean report: True ONLY if all expected steps are present exactly!
def verify_trajectory(expected: list[int], actual: list[int]) -> bool:
    pass
