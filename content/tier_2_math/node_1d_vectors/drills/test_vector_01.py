import pytest
import ex_vector_01 as active_lab

def test_vector_addition():
    ans = active_lab.add_vectors([1.0, 2.0], [3.0, 4.0])
    assert ans == [4.0, 6.0], "Vector addition failed. Ensure you are adding corresponding indices together in a loop."
