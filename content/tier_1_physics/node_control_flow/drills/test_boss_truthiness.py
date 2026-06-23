import pytest
import active_lab

def test_truthiness_classifier():
    assert active_lab.process_input(None) == 'missing', "Did you check explicitly for None using 'is None'?"
    assert active_lab.process_input(0) == 'zero', "Zero is falsy, but it is a valid integer. Check specifically for 0."
    assert active_lab.process_input([]) == 'empty_list', "An empty list should be identified as 'empty_list'."
    assert active_lab.process_input([1, 2]) == 'valid', "Populated lists are valid."
    assert active_lab.process_input("text") == 'valid', "Strings are valid."
