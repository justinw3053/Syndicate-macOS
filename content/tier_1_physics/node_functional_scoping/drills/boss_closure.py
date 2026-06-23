# BOSS FIGHT: Stateful Cost Tracker (Closure Factory)
# Closures allow a nested function to "remember" state from its enclosing scope.
# This is highly useful for tracking cumulative metrics (like API token costs) 
# without needing a full Object-Oriented class.
#
# Your Task: Complete the `make_cost_tracker()` factory.
# It should return a `tracker` function. 
# Every time the `tracker(tokens_to_add)` is called, it should:
# 1. Add `tokens_to_add` to `total_tokens`.
# 2. Calculate the cost ($0.000002 per token).
# 3. Return the cumulative total cost as a float.
# Note: You will need the `nonlocal` keyword to modify `total_tokens` inside the nested function.

def make_cost_tracker():
    total_tokens = 0
    def tracker(tokens_to_add: int) -> float:
        # STUDENT_IMPLEMENTATION: Implement a stateful closure using 'nonlocal'
        pass
    return tracker
