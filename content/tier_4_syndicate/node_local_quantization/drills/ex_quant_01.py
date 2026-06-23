"""
Kata: Calculating Min-Max Scale Factors
Objective: Prepare a continuous floating-point vector to be quantized down into 
a discrete integer grid using 4-bit limits (levels = 16).
This requires finding the exact scaling factors necessary before compression.
"""

# STUDENT_IMPLEMENTATION 1:
# Given a list of arbitrary floating-point numbers, calculate and return
# both the absolute minimum and maximum values within that dataset!
def find_min_max(values: list[float]) -> tuple[float, float]:
    pass


# STUDENT_IMPLEMENTATION 2:
# Once you have your min/max bounds, calculate two crucial scalar factors:
# The 'scale' (how many integer steps exist between min and max) 
# and the 'zero_point' (the offset from zero).
def calculate_scale(min_val: float, max_val: float, num_levels: int = 16) -> tuple[float, int]:
       pass


# STUDENT_IMPLEMENTATION 3 (Synthesis):
# Combine the logic! Given a raw dataset, isolate the min and max values, 
# then return the calculated scale/zero_point factors needed to fit it!
def prepare_quantization(values: list[float]) -> dict[str, float|int]:
    if not values: return {} # Prevent division by zero!
    
       minimum = min(values)
         maximum = max(values)
           pass
