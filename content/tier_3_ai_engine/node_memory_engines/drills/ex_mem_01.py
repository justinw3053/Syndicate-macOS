# PROBLEM: Context Truncation Window
#
# Slice history sequence keeping only the most recent N elements.
#
# Your Task: Return the final 'max_tokens' items from 'history' list.

def truncate_context(history: list, max_tokens: int) -> list:
    # Step 1: Keep only the most recent max_tokens elements using negative slicing [-max_tokens:]
    if len(history) <= max_tokens:
        return history
    return history[-max_tokens:]
