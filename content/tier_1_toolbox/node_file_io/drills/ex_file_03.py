# PROBLEM: Serializing to JSON Strings
#
# In web engineering, we convert dictionary data structures into text strings
# using the `json.dumps(dictionary)` function from the built-in json module.
#
# Your Task: Serialize the 'data' dictionary into a clean JSON string.

import json

def serialize_to_json(data: dict) -> str:
    # Step 1: Convert data dictionary to JSON string using json.dumps()
    json_string = json.dumps(data)
    return json_string
