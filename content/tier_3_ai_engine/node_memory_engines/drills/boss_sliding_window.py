# BOSS FIGHT: The Sliding Context Window
# When a chat history gets too long, we must truncate old messages to fit token limits.
# However, we must NEVER truncate the System prompt (which is always at index 0).
#
# Your Task: Implement slide_context(history, max_tokens, estimate_func)
# - If total tokens > max_tokens, remove the oldest messages (index 1, then 2...) 
#   until total <= max_tokens.
# - The system prompt (index 0) must remain untouched.

def slide_context(history: list[dict], max_tokens: int, estimate_func) -> list[dict]:
    # STUDENT_IMPLEMENTATION: Implement window sliding while locking in system prompt at index 0
    pass
