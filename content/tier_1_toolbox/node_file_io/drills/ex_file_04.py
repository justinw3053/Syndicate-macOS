# PROBLEM: Deserializing JSON payloads
#
# We load standard JSON text strings back into Python dictionaries using `json.loads(json_string)`.
#
# Your Task: Parse 'json_data' string and return the dictionary.

import json

def deserialize_from_json(json_data: str) -> dict:
    # Step 1: Parse JSON text using json.loads()
    data_dict = json.loads(json_data)
    return data_dict
