# PROBLEM: Dot Product (No Imports)
#
# Dot product sums the element-wise multiplications: `sum(a[0]*b[0] + a[1]*b[1] + ...)`
#
# Your Task: Compute the dot product of 'u' and 'v' from a loop.

def dot_product(u: list, v: list) -> float:
    assert len(u) == len(v), "Vectors must have identical dimensions!"
    total = 0.0
    # Step 1: Accumulate element-wise multiplications into total
    for i in range(len(u)):
        total += u[i] * v[i]
    return total
