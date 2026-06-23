# PROBLEM: Isolate shallow copy reference leakage
#
# A 'shallow copy' only duplicates the outer container. Any nested lists inside remain connected.
# To create a shallow copy of a dictionary, use: new_dict = old_dict.copy()
#
# Your Task: Complete the function below to return a shallow copy of 'base_config'.

def get_shallow_copy(base_config: dict) -> dict:
    # Step 1: Create a shallow copy of base_config using .copy()
    new_config = base_config.copy()
    
    # Step 2: Return your new_config
    return new_config
