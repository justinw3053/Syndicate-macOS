# PROBLEM: L2 Normalization (No Imports)
#
# L2 Norm (magnitude) is `sqrt(sum(x_i**2))`. Normalization divides each element by magnitude.
#
# Your Task: Normalize 'v' using L2 norm. Handle zero-division safely.

import math

def l2_normalize(v: list) -> list:
    # Step 1: Compute magnitude (L2 norm) of v
    sum_sq = sum(x ** 2 for x in v)
    magnitude = math.sqrt(sum_sq)
    
    # Step 2: Handle zero-division. If magnitude is 0, return v
    if magnitude == 0:
        return v
        
    # Step 3: Divide each item in v by magnitude and return
    return [x / magnitude for x in v]
