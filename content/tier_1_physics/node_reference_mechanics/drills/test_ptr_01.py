import pytest
import active_lab

def test_reference_isolation():
    assert active_lab.base_config["model"] == "qwen-2.5", "CRITICAL: Base config was mutated! Reference is still coupled."
    assert active_lab.user_config["model"] == "custom-agent", "CRITICAL: User config did not update its model."
