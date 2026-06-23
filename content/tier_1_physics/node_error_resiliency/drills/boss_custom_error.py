# BOSS FIGHT: Custom Domain Exceptions
# 'Inheriting' means creating a specialized sub-type that copies all behaviors from a 
# parent template class (e.g., creating a RateLimitError that acts like a standard Exception).
#
# Your Task: Define a 'RateLimitError' that inherits from 'Exception'.
# Then implement 'check_rate_limit(usage)'. If usage > 100, raise your new RateLimitError.
# Otherwise, return True.

# STUDENT_IMPLEMENTATION: Define RateLimitError

def check_rate_limit(usage: int) -> bool:
    # STUDENT_IMPLEMENTATION: Raise the error if usage > 100
    pass
