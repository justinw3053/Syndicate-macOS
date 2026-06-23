# PROBLEM: Compound Filtering and Sorting
#
# Your Task: Filter 'items' (list of dicts) keeping only those where 'status' is "active".
# Sort the matching items by the key "score" in descending order.

def filter_and_sort(items: list) -> list:
    # Step 1: Filter keeping only items where status == "active"
    filtered = [x for x in items if x.get("status") == "active"]
    
    # Step 2: Sort the filtered list by "score" in descending order
    sorted_list = sorted(filtered, key=lambda x: x.get("score", 0.0), reverse=True)
    return sorted_list
