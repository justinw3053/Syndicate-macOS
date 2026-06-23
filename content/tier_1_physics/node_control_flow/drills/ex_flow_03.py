# PROBLEM: Checking Subset Keys
#
# We can check if a key exists in a dict using the 'in' operator: `if key in my_dict:`
#
# Your Task: Return True if ALL keys in the 'required_keys' list exist in the 'config' dict.

def has_required_keys(config: dict, required_keys: list) -> bool:
    # Step 1: Loop through each required key
    for key in required_keys:
        # Step 2: If key is not in config, return False immediately
        if key not in config:
            return False
    # Step 3: If loop completes successfully, return True
    return True
