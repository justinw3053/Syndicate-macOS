# PROBLEM: Custom Exception domains
#
# Custom exceptions should inherit from the base Exception class.
#
# Your Task: Raise APIValidationError if validation checks fail.

class APIValidationError(Exception):
    pass

def validate_api_key(key: str):
    # Step 1: Validate key length and prefix
    if not key.startswith("sk-") or len(key) < 10:
        # Step 2: Raise custom exception if malformed
        raise APIValidationError("Invalid API Key format.")
