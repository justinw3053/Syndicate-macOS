import pytest
import boss_schema_validator as active_lab

def test_strict_validate():
    schema = {"name": str, "age": int}
    assert active_lab.strict_validate({"name": "Carl", "age": 5}, schema) == []
    
    errors = active_lab.strict_validate({"name": "Carl"}, schema)
    assert len(errors) == 1
    assert "Missing key" in errors[0]
