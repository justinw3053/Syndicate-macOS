import pytest
import active_lab

def test_mock_query():
    data = {"test": 123}
    res = active_lab.mock_server_query(data)
    assert res["status"] == "mock_success"
    assert res["payload"] == data
