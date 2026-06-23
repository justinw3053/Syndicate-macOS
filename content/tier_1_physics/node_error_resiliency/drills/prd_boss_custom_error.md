# PRD: Custom Domain Exceptions
Create a custom exception class named `RateLimitError` that inherits from `Exception`.
Then, write a function `check_rate_limit(requests: int)` that:
- Returns `True` if `requests < 100`.
- `raise`s a `RateLimitError` if `requests >= 100`.
