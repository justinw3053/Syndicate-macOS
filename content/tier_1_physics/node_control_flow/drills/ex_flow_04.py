# PROBLEM: Dynamic Dispatch Routing
#
# Dynamic dispatch uses dictionaries of functions instead of long if-elif chains:
#    actions = {"sum": lambda a,b: a+b}
#    res = actions[op](a,b)
#
# Your Task: Complete the routing function to look up 'op' and execute it.

def dispatch_operation(op: str, val: float) -> float:
    # Operations map:
    # "square" -> val ** 2
    # "negate" -> -val
    # "half" -> val / 2
    routes = {
        "square": lambda x: x ** 2,
        "negate": lambda x: -x,
        "half": lambda x: x / 2
    }
    
    # Step 1: Safely lookup 'op' in the routes dictionary using .get() with a default lambda returning val
    action = routes.get(op, lambda x: x)
    
    # Step 2: Execute the action and return the result
    return action(val)
