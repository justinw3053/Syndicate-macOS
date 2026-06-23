import pytest
import active_lab

def mock_estimate(text: str) -> int:
    # 1 token per word
    return len(text.split())

def test_sliding_window():
    history = [
        {"role": "system", "content": "You are helpful"}, # 3 tokens
        {"role": "user", "content": "Hello world"},       # 2 tokens
        {"role": "assistant", "content": "Hi there"},     # 2 tokens
        {"role": "user", "content": "Who am I?"}          # 3 tokens
    ] # Total: 10 tokens

    # Max 8: Should evict index 1 (Hello world) -> Total: 8
    res1 = active_lab.slide_context(list(history), 8, mock_estimate)
    assert len(res1) == 3
    assert res1[0]["role"] == "system"
    assert res1[1]["content"] == "Hi there"

    # Max 5: Should evict index 1 and 2 -> Total: 6... wait, to get <= 5 it must evict "Who am I?" too! Wait, if it evicts "Who am I", we only have system prompt left (3 tokens).
    res2 = active_lab.slide_context(list(history), 5, mock_estimate)
    assert len(res2) == 1
    assert res2[0]["role"] == "system"
