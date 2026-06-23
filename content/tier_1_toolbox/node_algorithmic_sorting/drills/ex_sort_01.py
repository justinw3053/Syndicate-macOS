# PROBLEM: Sorting Float Lists
#
# We sort collections in Python using `sorted(list)`.
# To sort in descending order (largest to smallest), pass the `reverse=True` parameter.
#
# Your Task: Implement `sort_logits(logits: list, descending: bool) -> list`

def sort_logits(logits: list, descending: bool) -> list:
    # Step 1: Sort list based on the descending flag
    sorted_list = sorted(logits, reverse=descending)
    return sorted_list
