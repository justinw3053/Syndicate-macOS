import pytest
import ex_vector_02 as active_lab

def test_hadamard_product():
    ans = active_lab.hadamard_product([2.0, 3.0], [4.0, 5.0])
    assert ans == [8.0, 15.0], "Hadamard product failed. Ensure you are multiplying corresponding indices together in a loop."
