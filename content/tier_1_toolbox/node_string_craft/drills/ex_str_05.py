# PROBLEM: Safe Substring Slicing
#
# We extract string segments using bracket slicing `[start:stop]`.
# If stop goes beyond the string length, Python handles it gracefully.
#
# Your Task: Return the first 'n' characters of 'prompt'. If 'n' is larger than prompt, return prompt.

def get_prefix_slice(prompt: str, n: int) -> str:
    # Step 1: Slice prompt from index 0 up to n using prompt[:n]
    prefix = prompt[:n]
    return prefix
