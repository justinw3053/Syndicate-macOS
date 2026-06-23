# PRD: The Token Primitive
Create a `Token` class from scratch.
- The constructor `__init__` should take a `text` string and a `prob` float.
- It must store these as instance variables `self.text` and `self.prob`.
- It must have a method `is_confident(threshold: float) -> bool` that returns True if the token's probability is greater than or equal to the threshold.
