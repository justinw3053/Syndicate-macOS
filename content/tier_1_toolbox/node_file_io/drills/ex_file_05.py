# PROBLEM: Portable Path Joining & Directory Generation
#
# Hardcoding path slashes (e.g. "folder/sub") crashes on Windows which uses backslashes `\`.
# We join paths portably using `os.path.join(a, b)` and check existence with `os.path.exists()`.
#
# Your Task:
# 1. Join 'base_dir' and 'filename' portably.
# 2. Check if the directory 'base_dir' exists. If it does not, create it using `os.makedirs(base_dir)`.
# 3. Return the fully joined path.

import os

def resolve_and_create_path(base_dir: str, filename: str) -> str:
    # Step 1: Check if base_dir exists using os.path.exists()
    if not os.path.exists(base_dir):
        # Step 2: Create directories if missing using os.makedirs()
        os.makedirs(base_dir)
        
    # Step 3: Join base_dir and filename portably using os.path.join()
    full_path = os.path.join(base_dir, filename)
    return full_path
