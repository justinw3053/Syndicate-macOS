import pytest
import ex_error_01 as active_lab

def test_parse_payload():
    good_payload = "{"model": "gpt-4"}"
    assert active_lab.parse_payload(good_payload)["model"] == "gpt-4", "Valid JSON payloads should parse successfully without error."
