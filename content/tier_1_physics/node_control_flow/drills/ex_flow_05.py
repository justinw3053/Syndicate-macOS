# PROBLEM: Range step limits
#
# The range function takes start, stop, and step: `range(start, stop, step)`
#
# Your Task: Return a list of odd numbers between 'start' and 'stop' (inclusive).

def get_odds(start: int, stop: int) -> list:
    # Step 1: Ensure start is odd. If start is even, add 1 to it.
    if start % 2 == 0:
        start += 1
        
    # Step 2: Use range() with a step of 2 to generate odd numbers up to stop + 1
    odds = list(range(start, stop + 1, 2))
    return odds
