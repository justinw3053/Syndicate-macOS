import pytest
import active_lab

def test_closure():
    track = active_lab.make_cost_tracker()
    
    cost1 = track(100)
    assert cost1 == 0.0002, f"Expected 0.0002, got {cost1}"
    
    cost2 = track(200)
    assert cost2 == 0.0006, f"Expected 0.0006. Did the closure remember the previous 100 tokens? You need the 'nonlocal' keyword."
    
    # Ensure a separate tracker maintains its own independent state
    track_b = active_lab.make_cost_tracker()
    assert track_b(50) == 0.0001, "A newly initialized tracker should start at 0."
