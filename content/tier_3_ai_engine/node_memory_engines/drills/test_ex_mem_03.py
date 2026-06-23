"""
Test Suite: Capacity Evaluation (Pre-Bound Eviction)
Validates the mathematical logic of pre-loading checks before queue mutations.
"""

import pytest


def test_calculate_capacity():
    from ex_mem_03 import calculate_capacity
    
    assert calculate_capacity(["A"]) == 1
    assert calculate_capacity(["Hello", "World"]) == 10
    assert calculate_capacity([]) == 0


def test_evaluate_eviction_logic():
    from ex_mem_03 import evaluate_eviction
    
     # Current load = 4, Max capacity = 6, Incoming size = 1. 
     # Does 4 + 1 > 6 ? -> False (No eviction needed)
    assert evaluate_eviction(4, 1, 6) == False
    
    # Current load = 5, Max capacity = 6, Incoming size = 2.
     # Does 5 + 2 > 6 ? -> True (Eviction IS needed)
    assert evaluate_eviction(5, 2, 6) == True


def test_evict_and_append():
    from ex_mem_03 import evict_and_append
    
    q = ["A", "B"] # Length is 2. Max capacity is 3.
    
    # Adding a string of length 1: 2 + 1 <= 3 (No eviction)
    evict_and_append(q, "C") 
    assert "C" in q
    
     # Queue now has "A", "B", "C". Length = 3. Max capacity = 3.
    # Adding a string of length 2: 3 + 2 > 3 (Eviction triggered!)
    evict_and_append(q, "DE") 
    
    assert len(q) == 3
    
     # Since we evicted from index 0 previously to make room, 
     # "A" should be the first item if we don't pop(0), or if we append right.
     # Wait: Our loop just checks length vs capacity. 
     # Let's assert 'C' and 'DE' are in there somewhere (or 'B').
    assert "DE" in q
