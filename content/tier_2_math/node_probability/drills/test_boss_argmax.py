import pytest
import boss_argmax as active_lab

def test_argmax():
    probs = [0.1, 0.6, 0.2, 0.1]
    assert active_lab.argmax(probs) == 1, "Expected index 1 (value 0.6)"
    
    with pytest.raises(ValueError):
        active_lab.argmax([])
