# PROBLEM: Deep copy decoupling
#
# A 'deep copy' recursively duplicates all elements, fully isolating nested lists/dicts.
# First, import the built-in copy module: `import copy`
# Then, use the deepcopy function: `new_obj = copy.deepcopy(old_obj)`
#
# Your Task: Complete the function below to return a deep copy of 'complex_config'.

import copy

def get_deep_copy(complex_config: dict) -> dict:
    # Step 1: Create a deep copy of complex_config using copy.deepcopy()
    isolated_config = copy.deepcopy(complex_config)
    
    # Step 2: Return your isolated_config
    return isolated_config
