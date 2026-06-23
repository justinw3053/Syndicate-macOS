import pytest
import active_lab

def test_deserialize():
    raw = '{"model": "llama", "tokens": 10}'
    assert active_lab.deserialize_from_json(raw) == {"model": "llama", "tokens": 10}
