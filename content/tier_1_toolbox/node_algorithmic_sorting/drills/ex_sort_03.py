# PROBLEM: Extracting the Largest Element Value Index (Argmax)
#
# Finding the index of the highest score is called "Argmax".
#
# Your Task: Return the index (position) of the largest float inside 'logits'.
# Handle empty list: if logits is empty, return -1.

def extract_argmax_index(logits: list) -> int:
    if not logits:
        return -1
        
    # Step 1: Find the maximum value in logits
    max_val = max(logits)
    
    # Step 2: Use .index() to find the index of max_val and return it
    max_idx = logits.index(max_val)
    return max_idx
