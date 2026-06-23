# PROBLEM: Nested Dictionary Safely Traversal
#
# Safely extract deeply nested keys using multiple .get() fallback maps.
#
# Your Task: Safely extract the API key: `config -> "api" -> "key"`. Return "missing" if absent.

def get_nested_api_key(config: dict) -> str:
    # Step 1: Safely get the "api" dictionary using .get()
    api_dict = config.get("api", {})
    if not isinstance(api_dict, dict):
        return "missing"
        
    # Step 2: Safely extract "key" from the api_dict, fallback to "missing"
    api_key = api_dict.get("key", "missing")
    return api_key
