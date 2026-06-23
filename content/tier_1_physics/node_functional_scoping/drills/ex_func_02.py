# PROBLEM: Mutable Default Argument Leakage
#
# In Python, using lists or dicts directly as default arguments (e.g. `def run(lst=[])`)
# causes leakage because the default list is created only once on compile.
# Fix this by setting default to None and instantiating inside the body.
#
# Your Task: Safely initialize the default list to prevent leakage.

def append_to_list(item, target_list: list = None) -> list:
    # Step 1: If target_list is None, set target_list to a fresh empty list []
    if target_list is None:
        target_list = []
        
    # Step 2: Append item and return target_list
    target_list.append(item)
    return target_list
