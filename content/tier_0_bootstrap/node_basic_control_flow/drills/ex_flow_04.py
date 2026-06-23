# EXERCISE 9: Accumulating Totals in Loops
#
# To sum up numbers inside a loop, we create an "accumulator" variable set to 0.0
# before the loop, and add to it inside the loop using the addition operator:
#    total = 0.0
#    for num in my_list:
#        total += num    # Adds the current number to the total
#
# Your Task:
# Create a variable named 'total' and initialize it to 0.0.
# Loop through the list of 'numbers' using a 'for' loop.
# Inside the loop, add each 'num' directly to 'total'.
# Return 'total' at the very end of the function.

def sum_all_numbers(numbers):
    # Initialize total below
    total = ...
    
    # Complete the loop and accumulator step
    for num in ...:
        total += ...
        
    return total
