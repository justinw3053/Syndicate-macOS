# PROBLEM: Euclidean Distance (No Imports)
#
# Euclidean distance is the square root of the sum of squared differences.
# Formula: `sqrt(sum((u[i] - v[i])**2))`
#
# Your Task: Compute Euclidean distance between 'u' and 'v'.

import math

def euclidean_distance(u: list, v: list) -> float:
    assert len(u) == len(v), "Vectors must have identical dimensions!"
    sum_squares = 0.0
    # Step 1: Sum the squared differences between corresponding items
    for i in range(len(u)):
        sum_squares += (u[i] - v[i]) ** 2
    # Step 2: Take and return square root of sum_squares
    return math.sqrt(sum_squares)
