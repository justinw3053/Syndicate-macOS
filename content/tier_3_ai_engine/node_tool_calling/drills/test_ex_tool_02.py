import pytest
import ex_tool_02 as active_lab

def add(a, b): return a + b

def test_execute_tool():
    reg = {"add": add}
    assert active_lab.execute_tool("add", {"a": 5, "b": 3}, reg) == 8, "Execution failed. Did you unpack the arguments using **args?"
    assert active_lab.execute_tool("sub", {}, reg) == "Error: Tool not found", "Crash detected. You must use a try/except block to catch KeyErrors and return the error string."
