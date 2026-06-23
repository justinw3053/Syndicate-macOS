"""
Kata: Non-Overlapping Sliding List Chunker
Objective: Implement an absolute baseline chunker that slices a list into 
disjoint, non-overlapping segments of size `N`.
This mimics early-stage document retrieval strategies without context bleeding.
"""

# STUDENT_IMPLEMENTATION 1:
# Given a target chunk size (e.g., 3) and the total length of a list,
# return how many complete chunks can be extracted before we run out of elements!
def calculate_chunk_count(list_len: int, chunk_size: int) -> int:
    pass


# STUDENT_IMPLEMENTATION 2:
# Given a strictly non-overlapping starting position (0, 3, 6...), 
# slice an array from `start` to `start + chunk_size`. 
# If fewer than `chunk_size` elements remain, slice only what is left!
def safe_slice(data: list[any], start_pos: int, chunk_size: int) -> list[any]:
       pass


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Iterate through an array `data` using a step size of `chunk_size`. 
# Extract each slice into a parent list!
def generate_slices(data: list[any], chunk_size: int) -> list[list[any]]:
    return []
