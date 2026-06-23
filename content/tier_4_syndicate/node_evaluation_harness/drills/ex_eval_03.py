"""
Kata: List Adjacency Validation (Trajectory Auditing)
Objective: Verify that a sequence of states strictly follows the expected adjacency rules.
This represents evaluating a trajectory to see if an LLM jumped from State A directly to State C without passing through State B.
"""

# STUDENT_IMPLEMENTATION 1:
# Given a list representing a sequential trajectory (e.g., [0, 1, 2, 3]),
# verify that the absolute difference between any two adjacent elements is ALWAYS exactly 1.
def validate_adjacency(strict_seq: list[int]) -> bool:
    pass


# STUDENT_IMPLEMENTATION 2:
# Given an expected sequential adjacency map and an actual returned trajectory,
# determine if the actual sequence perfectly matches step-by-step.
def strict_match(expected: list[int], actual: list[int]) -> bool:
      pass


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Build a robust validation function that takes multiple strictly sequential trajectories 
# and returns False immediately if any single trajectory violates adjacency!
def validate_all(trajs: list[list[int]]) -> bool:
     for traj in trajs:
        pass
    
       return True
