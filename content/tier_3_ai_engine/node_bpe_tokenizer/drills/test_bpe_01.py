import pytest
import active_lab
def test_string_to_bytes():
    byte_ints = active_lab.string_to_bytes('Hello 👋')
    assert len(byte_ints) == 10
    assert byte_ints[:5] == [72, 101, 108, 108, 111]
    assert byte_ints[6:] == [240, 159, 145, 139]
