# PROBLEM: Scaled Dot-Product Attention (No Imports)
#
# Compute attention: `softmax(Q * K_T / sqrt(d_k)) * V`
#
# Your Task: Implement scaled attention for single dimension float matrices.

import math

def scaled_dot_product_attention(Q: list, K: list, V: list, d_k: float) -> list:
    # Step 1: Compute similarity scores: Q * K transposed (dot product)
    scores = [sum(Q[i] * K[i] for i in range(len(Q)))]
    
    # Step 2: Scale scores by square root of d_k
    scaled_scores = [x / math.sqrt(d_k) for x in scores]
    
    # Step 3: Apply Softmax and multiply by V
    max_score = max(scaled_scores)
    exps = [math.exp(x - max_score) for x in scaled_scores]
    sum_exps = sum(exps)
    probs = [x / sum_exps for x in exps]
    
    return [probs[0] * val for val in V]
