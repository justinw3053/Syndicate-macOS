import pytest
import ex_dict_02 as active_lab

def test_build_registry():
    tools = [{"id": "calc", "name": "Calculator"}, {"id": "search", "name": "Web"}]
    registry = active_lab.build_registry(tools)
    assert len(registry) == 2, "The registry should contain exactly 2 tools."
    assert registry["calc"]["name"] == "Calculator", "Failed to map id to the correct tool dictionary."
