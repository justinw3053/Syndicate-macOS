# PROBLEM: Dictionary Comprehension
#
# Dict comprehensions map key-value pairs: `{k: v for k, v in my_dict.items() if v > 0}`
#
# Your Task: Filter the 'config' dictionary, keeping only keys where value is greater than 10.

def filter_config(config: dict) -> dict:
    # Step 1: Filter config dictionary keeping values > 10 using a dict comprehension
    filtered = {k: v for k, v in config.items() if v > 10}
    return filtered
