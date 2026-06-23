# PROBLEM: List Comprehension with Conditions
#
# Comprehensions are elegant ways to build lists: `[num for num in numbers if num > 5]`
#
# Your Task: Return a new list containing only positive numbers from 'numbers'.

def get_positives(numbers: list) -> list:
    # Step 1: Use a list comprehension to filter positive numbers (> 0)
    positives = [num for num in numbers if num > 0]
    return positives
