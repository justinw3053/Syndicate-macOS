import pytest
from active_lab import StateManager

def test_state_extraction_is_deep_copy():
    manager = StateManager({"theme": "dark", "plugins": ["lint", "format"]})
    state_copy = manager.get_state()
    state_copy["theme"] = "light"
    state_copy["plugins"].append("git")
    
    internal_state = manager.get_state()
    assert internal_state["theme"] == "dark", "State corruption! get_state() returned a mutable reference."
    assert "git" not in internal_state["plugins"], "State corruption! get_state() leaked a nested list reference."

def test_state_update_decouples_reference():
    manager = StateManager({"theme": "dark", "plugins": ["lint", "format"]})
    new_config = {"theme": "light", "plugins": ["git"]}
    manager.update_state(new_config)
    
    new_config["theme"] = "broken"
    assert manager.get_state()["theme"] == "light", "State corruption! update_state() bound to a mutable external reference."
