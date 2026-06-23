# PROBLEM: Cosine Similarity Metric
#
# Cosine Similarity measures angular proximity: `dot_product(u,v) / (norm(u) * norm(v))`
#
# Your Task: Compute cosine similarity between 'u' and 'v'. Handle zero division.

import math

def cosine_similarity(u: list, v: list) -> float:
    # Step 1: Compute dot product
    dot_prod = sum(u[i] * v[i] for i in range(len(u)))
    
    # Step 2: Compute L2 Norms
    norm_u = math.sqrt(sum(x ** 2 for x in u))
    norm_v = math.sqrt(sum(x ** 2 for x in v))
    
    # Step 3: Handle zero division safeguards
    if norm_u == 0 or norm_v == 0:
        return 0.0
        
    return dot_prod / (norm_u * norm_v)
