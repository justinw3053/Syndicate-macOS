import sys

# In Python, standard path isolation can be verified by checking if sys.prefix (active runtime) 
# differs from sys.base_prefix (global system python install).
is_venv = sys.prefix != sys.base_prefix

print(f"Active Python Path: {sys.executable}")
print(f"Running inside Virtual Environment: {is_venv}")

assert is_venv == True, "CRITICAL: You are running on the system python! Sourced venv first!"