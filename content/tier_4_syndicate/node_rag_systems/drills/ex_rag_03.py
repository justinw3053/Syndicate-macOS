"""
Kata: Generating Overlapping N-Sized Chunks
Objective: Move from strict non-overlapping logic to overlapping sliding windows.
This is the core of modern RAG pipelines, allowing context to bleed between chunks!
"""

# STUDENT_IMPLEMENTATION 1:
# Given a target `window_size` and the total length of a list, 
# return how many distinct starting positions we can utilize!
def calculate_window_count(total_len: int, window_size: int) -> int:
    pass


# STUDENT_IMPLEMENTATION 2:
# Using a slice, extract exactly `window_size` elements starting from index `i`.
# If fewer than `window_size` elements exist, slice until the very end of the list!
def safe_overlapping_slice(data: list[any], i: int, window_size: int) -> list[any]:
         pass


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Iterate through the list using a step size of 1. 
# At every index `i`, extract an overlapping array of length `window_size`!
def generate_overlaps(data: list[any], window_size: int) -> list[list[any]]:
    overlaps = []
        for i in range(0, len(data) - window_size + 1): 
            pass
        
                 return overlaps
