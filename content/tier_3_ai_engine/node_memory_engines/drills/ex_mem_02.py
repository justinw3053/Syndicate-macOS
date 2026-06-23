# PROBLEM: Retain System Parameters (Pinned Context)
#
# Ensure system messages pinned at index 0 are preserved during context window truncation.
#
# Your Task: Truncate history keeping index 0 (system) intact at the front.

def truncate_with_system(history: list, max_tokens: int) -> list:
    if len(history) <= max_tokens:
        return history
    # Step 1: Preserve system message (index 0)
    system_msg = history[0]
    
    # Step 2: Truncate the remaining messages to fit within the remaining max_tokens - 1 slots
    remaining = history[1:]
    truncated_remaining = remaining[-(max_tokens - 1):]
    
    # Step 3: Concatenate and return
    return [system_msg] + truncated_remaining
