# PROBLEM: List Slicing Mechanics
# Context windows require truncating old messages. 
# `my_list[start:end]` returns a new list containing elements from `start` up to (but not including) `end`.
#
# Your Task: Implement `truncate_oldest(history: list, max_length: int) -> list`
# If `history` is longer than `max_length`, use slicing to return ONLY the newest `max_length` items.
# If it is shorter, return the whole list.

def truncate_oldest(history: list, max_length: int) -> list:
    pass # STUDENT_IMPLEMENTATION: Implement using list slicing
