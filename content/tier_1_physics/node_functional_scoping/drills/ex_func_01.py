# PROBLEM: Closures and State factories
#
# A closure is an inner function that remembers and accesses variables in its outer scope.
#
# Your Task: Implement a state factory counter that adds 'step' to a count on every call.

def create_counter(start: int, step: int):
    count = start
    
    def counter():
        nonlocal count
        # Step 1: Add step to count
        count += step
        # Step 2: Return current count
        return count
        
    return counter
