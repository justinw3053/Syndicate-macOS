import pytest
import ex_vector_05 as active_lab

def test_normalize():
    vec = [3, 4]
    norm = active_lab.normalize(vec)
    assert abs(norm[0] - 0.6) < 1e-9 and abs(norm[1] - 0.8) < 1e-9, "Math is incorrect. Did you divide by magnitude (5.0)?"
    
    with pytest.raises(ValueError):
        active_lab.normalize([0, 0])
