# PRD: The Sliding Context Window

## Overview
Models have strict context limits. You must implement a FIFO (First-In, First-Out) sliding window that safely truncates old conversational turns while cryptographically locking the initial System directives.

## Requirements
1.  Implement `slide_context(history: list, max_tokens: int, estimate_func) -> list`.
2.  `estimate_func(text: str)` returns the token count.
3.  Calculate the total token cost of all messages in `history`.
4.  If the total exceeds `max_tokens`, evict the oldest conversational message (index `1`).
5.  Repeat eviction until the total token count is `<= max_tokens`.
6.  The element at index `0` (the System Prompt) must NEVER be evicted, even if its isolated cost exceeds `max_tokens`.
