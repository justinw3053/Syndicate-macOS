# PROBLEM: Numerical Stability and log-sum-exp trick
#
# Log-Sum-Exp avoids overflow by subtracting max values before exponents.
#
# Your Task: Compute log-sum-exp of 'logits' safely.

import math

def log_sum_exp(logits: list) -> float:
    # Step 1: Find max logit value
    max_logit = max(logits)
    
    # Step 2: Subtract max_logit and exponentiate
    sum_exps = sum(math.exp(x - max_logit) for x in logits)
    
    # Step 3: Compute final log-sum-exp: max_logit + log(sum_exps)
    return max_logit + math.log(sum_exps)
