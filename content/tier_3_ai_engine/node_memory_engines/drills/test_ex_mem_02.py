"""
Test Suite: Conditional Mutation & State Safety (ex_mem_02)
Validates the logic of locking index 0 (System Prompt) while sliding context.
"""

import pytest


class TestLockIndexZero:
    def test_add_turn_appends(self):
        from ex_mem_02 import add_turn
        
        contexts = [["You are a helpful assistant"]] # index 0 is system prompt
        
        add_turn(contexts, "user", "Hello")
        add_turn(contexts, "assistant", "Hi there!")
        
        assert len(contexts) == 3


    def test_evict_oldest_keeps_system_prompt(self):
        from ex_mem_02 import evict_oldest
        
        contexts = [
            ["System Prompt"], # index 0 must NEVER be evicted
            ["User Turn 1"],
            ["Assistant Turn 1"]
        ]
        
        evict_oldest(contexts)
        
        assert len(contexts) == 2
        assert contexts[0] == ["System Prompt"]


class TestProcessTurns:
    def test_process_turns_enforces_max_history(self):
        from ex_mem_02 import process_turns
        
        # Start with max_history = 2. Total capacity allowed = 3 items (1 system + 2 history)
        contexts = [
            ["System Prompt"], 
            ["User Turn 1"],
            ["Assistant Turn 1"]
            # If we add one more, the oldest user turn must vanish!
        ]
        
        process_turns(contexts, "user", "New User Turn", max_history=2)
        
        assert len(contexts) == 3
        # The first item ALWAYS remains as the System Prompt
        assert contexts[0] == ["System Prompt"]
        # The new user turn is at index 1!
        assert contexts[1][0] == "User Turn 1" # Wait, let me re-read logic.
