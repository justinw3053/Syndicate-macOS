# PROBLEM: Embedding Matrix Projection
#
# Projection multiplies a flat vector by an embedding projection weights matrix.
#
# Your Task: Multiply input vector 'v' by weights matrix 'W' (shape: dimensions x vocab_size).

def project_embedding(v: list, W: list) -> list:
    res = []
    # Step 1: Map matrix dimensions (columns)
    for col in range(len(W[0])):
        # Step 2: Multiply v with column col of matrix W
        val = sum(v[row] * W[row][col] for row in range(len(v)))
        res.append(val)
    return res
