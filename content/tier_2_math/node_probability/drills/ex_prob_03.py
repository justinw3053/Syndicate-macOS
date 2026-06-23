# PROBLEM: Top-K Masking (Logits Boundary Filter)
#
# Top-K retains only the largest K values, setting all others to negative infinity.
#
# Your Task: Filter 'logits', keeping only top 'k' elements.

def top_k_mask(logits: list, k: int) -> list:
    # Step 1: Find value of the k-th largest logit
    sorted_logits = sorted(logits, reverse=True)
    k_threshold = sorted_logits[k - 1]
    
    # Step 2: Set any logit strictly below k_threshold to float('-inf')
    res = []
    for x in logits:
        if x < k_threshold:
            res.append(float('-inf'))
        else:
            res.append(x)
    return res
