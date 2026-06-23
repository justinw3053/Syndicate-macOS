import pytest
import ex_tool_01 as active_lab

def test_extract_types():
    hints = {"name": str, "age": int, "is_active": bool}
    res = active_lab.extract_types(hints)
    assert res["name"] == "string"
    assert res["age"] == "integer"
    assert res["is_active"] == "boolean"
