# PROBLEM: Softmax with Temperature Scaling
#
# Softmax scales logits to probability: `exp(x_i / T) / sum(exp(x_j / T))`
#
# Your Task: Apply temperature-scaled Softmax to 'logits'.

import math

def softmax_temperature(logits: list, temp: float) -> list:
    # Step 1: Temperature-scale logits
    scaled = [x / temp for x in logits]
    
    # Step 2: Prevent exponential overflow by subtracting max scaled value
    max_val = max(scaled)
    shifted = [x - max_val for x in scaled]
    
    # Step 3: Exponentiate and normalize
    exps = [math.exp(x) for x in shifted]
    sum_exps = sum(exps)
    
    return [x / sum_exps for x in exps]
