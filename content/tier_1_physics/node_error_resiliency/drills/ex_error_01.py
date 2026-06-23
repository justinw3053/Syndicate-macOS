# PROBLEM: Finally Block Execution
#
# The finally block executes cleanup code unconditionally, regardless of success or crash.
#
# Your Task: Complete the runner function. Ensure 'cleanup' executes in finally.

def execute_with_cleanup(operation_lambda, cleanup_lambda):
    try:
        # Step 1: Run the operation
        return operation_lambda()
    finally:
        # Step 2: Ensure cleanup runs unconditionally
        cleanup_lambda()
