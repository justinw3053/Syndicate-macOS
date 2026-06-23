import pytest
import active_lab

def test_deep_copy_isolation():
    assert "health" in active_lab.inventory["potions"], "CRITICAL: The master inventory was mutated! Shallow copy leaked the nested list reference."
    assert "health" not in active_lab.player_inventory["potions"], "CRITICAL: The player inventory did not remove the potion."
