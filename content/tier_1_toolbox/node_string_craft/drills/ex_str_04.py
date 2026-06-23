# PROBLEM: Joining String Sequences
#
# We merge lists of strings back into a single string using `.join()` called on the glue:
# Example: `",".join(["a", "b", "c"])` returns `"a,b,c"`.
#
# Your Task: Join the list of 'tokens' together using a single space character " " as glue.

def join_tokens(tokens: list) -> str:
    # Step 1: Join tokens with space " " as the glue string
    joined = " ".join(tokens)
    return joined
