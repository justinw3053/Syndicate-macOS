"""
Test Suite: FIFO Queue Mechanics (ex_mem_01)
Validates that the basic pointer manipulations and error handling are correct.
"""

import pytest
from ex_mem_01 import enqueue, dequeue, peek


def test_fifo_enqueue_appends():
    q = []
    enqueue(q, "A")
    assert len(q) == 1
    assert q[0] == "A"
    
    enqueue(q, "B")
    enqueue(q, "C")
    items = [q.pop(0), q.pop(0), q.pop(0)]
    assert items == ["A", "B", "C"]


def test_fifo_dequeue_removes():
    q = ["X", "Y"]
    item = dequeue(q)
    assert item == "X"
    assert len(q) == 1
    
    with pytest.raises(ValueError):
        dequeue(q)


def test_peek_returns_without_removing():
    q = []
    enqueue(q, "Z")
        
    assert peek(q) == "Z"
      # Assert that Z is STILL in the queue (length didn't drop to zero)
    assert len(q) == 1
