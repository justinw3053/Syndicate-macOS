# PROBLEM: Sequence Slicing & Sliding Windows
#
# Python lists support slicing operations: `list_obj[start:stop:step]`
#
# Your Task: Return a sub-list of 'history' from index 'start' to 'stop' (exclusive).

def slice_history(history: list, start: int, stop: int) -> list:
    # Step 1: Slice history sequence cleanly
    return history[start:stop]
