# PROBLEM: Dynamic Type Checking
#
# When parsing dynamic schemas, check types safely using isinstance(obj, type).
# Example: isinstance(val, str) checks if val is text.
#
# Your Task: Implement `filter_strings(data: list) -> list` to return ONLY strings from 'data'.

def filter_strings(data: list) -> list:
    strings = []
    # Step 1: Iterate through data using a for loop
    for item in data:
        # Step 2: Check if item is a string using isinstance(item, str)
        if isinstance(item, str):
            # Step 3: Append the matching item to strings
            strings.append(item)
    return strings
