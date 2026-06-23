# PRD: Dual Bounds Tracking
## Overview
In neural networks, we regularly analyze arrays of raw scores (logits). Often, we want to accumulate a total while tracking both the smallest (minimum) and largest (maximum) values in a single execution pass.
## Requirements
1.  Iterate over the list scores = [2.3, -1.5, 4.2, 0.0, -3.1, 1.8].
2.  Calculate the running sum and store it in running_sum.
3.  Find the minimum value and store it in min_score.
4.  Find the maximum value and store it in max_score.
## Constraints
- You MUST compute all three metrics in a single loop.
- You MUST NOT use Python built-in sum, min or max functions.
