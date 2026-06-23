import pytest
import active_lab
def test_enforced_buffer():
    buffer = active_lab.PromptBuffer()
    buffer.append('System online.')
    buffer.append('User connected.')
    assert len(buffer) == 2, '__len__ not implemented correctly.'
    with pytest.raises(TypeError):
        buffer.append(404)
