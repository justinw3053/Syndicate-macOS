# PROBLEM: Splitting Text by Delimiters
#
# We partition raw log lines or parameter sequences using the `.split(delimiter)` method.
# Example: `"a,b,c".split(",")` returns the list `["a", "b", "c"]`.
#
# Your Task: Split 'raw_data' by the pipe character '|' and return the list of parts.

def split_parameters(raw_data: str) -> list:
    # Step 1: Split raw_data using the delimiter '|'
    parts = raw_data.split("|")
    return parts
