import sys

# In Python, standard path isolation can be verified by checking if sys.prefix (active runtime) 
# differs from sys.base_prefix (global system python install).
is_venv = sys.prefix != sys.base_prefix

print(f"Active Python Path: {sys.executable}")
print(f"Running inside Virtual Environment: {is_venv}")

assert is_venv == True, "CRITICAL: You are running on the system python! Sourced venv first!"

import sys

major = sys.version_info.major
minor = sys.version_info.minor

print(f"Active Executable: {sys.executable}")
print(f"Python Version: {major}.{minor}")

# TODO: Write assertions to confirm that we are running Python 3 (major == 3) and at least minor version 8 (minor >= 8).
# Your code here:


assert major == 3, "CRITICAL: You are not running Python 3!"
assert minor >= 8, "CRITICAL: Syndicate 3.0 requires Python 3.8+!"
print("Success! Python version validation passed.")