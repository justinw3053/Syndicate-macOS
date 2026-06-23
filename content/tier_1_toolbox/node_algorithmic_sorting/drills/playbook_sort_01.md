# Textbook: Sorting Float Lists (KATA_SORT_01)

## Theoretical Foundation
During token generation, models output arrays of log-probabilities (logits). To locate which words are the most probable, we sort the score arrays. The standard `sorted()` function returns a fresh sorted list, preserving the original array in memory.

---

## Step-by-Step Exercise Instructions
1. Pass the `logits` list to the `sorted()` function.
2. Use the `reverse=descending` parameter to control sort orientation.
3. Return the sorted list.
