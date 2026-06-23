# PROBLEM: Hadamard Product (No Imports)
#
# Hadamard product computes element-wise multiplication: `[a[0]*b[0], a[1]*b[1], ...]`
#
# Your Task: Multiply elements of 'u' and 'v' correspondingly.

def hadamard_product(u: list, v: list) -> list:
    assert len(u) == len(v), "Vectors must have identical dimensions!"
    res = []
    # Step 1: Multiply corresponding elements at index i and append
    for i in range(len(u)):
        res.append(u[i] * v[i])
    return res
