# PROBLEM: Payload Routing with Error Resiliency
# When the LLM outputs a tool call, it provides a tool name and arguments.
# We must route this to the actual python function.
#
# Your Task: Implement execute_tool(tool_name: str, args: dict, registry: dict) -> any
# Find the function in the registry by name, and execute it by unpacking the kwargs.
# CRITICAL: You must use a try/except block. If a KeyError occurs (tool doesn't exist),
# catch it and return the string "Error: Tool not found". Do not let the program crash.

def execute_tool(tool_name: str, args: dict, registry: dict):
    # STUDENT_IMPLEMENTATION: Use try/except to execute or gracefully fail
    pass
