# PROBLEM: Lexical LEGB Lookup
#
# Resolving variables flows: Local -> Enclosing -> Global -> Built-in.
#
# Your Task: Safely read global and local variables to return the absolute difference.

import math

# Global threshold definition
THRESHOLD = 10.0

def calculate_threshold_diff(val: float) -> float:
    # Step 1: Compute absolute difference between local 'val' and global 'THRESHOLD'
    diff = abs(val - THRESHOLD)
    return diff
