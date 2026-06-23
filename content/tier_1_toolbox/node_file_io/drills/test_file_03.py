import pytest
import active_lab
import json

def test_serialize():
    cfg = {"model": "qwen", "temp": 0.7}
    res = active_lab.serialize_to_json(cfg)
    assert json.loads(res) == cfg
