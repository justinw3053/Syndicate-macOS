# PROBLEM: Dictionary Merging
#
# Merge dictionaries using the unpack operator `**`: `merged = {**dict1, **dict2}`
#
# Your Task: Merge 'default_config' and 'user_config'. 'user_config' must override defaults.

def merge_configs(default_config: dict, user_config: dict) -> dict:
    # Step 1: Merge default_config and user_config using dict unpacking
    merged = {**default_config, **user_config}
    return merged
