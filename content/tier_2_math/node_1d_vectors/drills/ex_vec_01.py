# PROBLEM: Vector Addition (No Imports)
#
# Vector addition sum elements at corresponding indices: `[a[0]+b[0], a[1]+b[1], ...]`
#
# Your Task: Add two vectors 'u' and 'v' of identical shape together using a loop.

def vector_addition(u: list, v: list) -> list:
    assert len(u) == len(v), "Vectors must have identical dimensions!"
    res = []
    # Step 1: Loop through indices up to length of u
    for i in range(len(u)):
        # Step 2: Sum corresponding elements and append
        res.append(u[i] + v[i])
    return res
