import pytest
import ex_tool_03 as active_lab

def test_coerce_args():
    args = {"age": "42", "active": "True"}
    schema = {"age": "integer", "active": "boolean"}
    res = active_lab.coerce_args(args, schema)
    assert res["age"] == 42
    assert res["active"] is True
