import pytest
import active_lab
def test_cosine_similarity():
    q = [1.0, 0.0]
    doc_a = [4.0, 0.0]
    doc_b = [1.0, 1.0]
    sim_a = active_lab.cosine_similarity(q, doc_a)
    sim_b = active_lab.cosine_similarity(q, doc_b)
    assert abs(sim_a - 1.0) < 1e-6
    assert abs(sim_b - 0.707106) < 1e-4
