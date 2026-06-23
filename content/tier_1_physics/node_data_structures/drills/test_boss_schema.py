import pytest
import active_lab

def test_schema_validator():
    assert active_lab.validate_tool_schema({'id': '1', 'name': 'test', 'params': ['a']}) == True, "Valid payload should return True."
    assert active_lab.validate_tool_schema({'id': '1', 'name': 'test'}) == False, "Missing 'params' key should fail."
    assert active_lab.validate_tool_schema({'id': 1, 'name': 'test', 'params': []}) == False, "'id' must be a string, not an int."
    assert active_lab.validate_tool_schema({'id': '1', 'name': 'test', 'params': [], 'extra': 1}) == False, "Extra keys should cause validation to fail."
