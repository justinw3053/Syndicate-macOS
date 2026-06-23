import pytest
import ex_dict_01 as active_lab

def test_dict_extraction():
    assert active_lab.assistant_content == "hi", "Extraction failed. Remember to combine list indexing and key-lookup: payload["messages"][1]["content"]."
