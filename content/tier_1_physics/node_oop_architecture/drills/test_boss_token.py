import pytest
import boss_token as active_lab

def test_token_primitive():
    token = active_lab.Token("hi", 0.9)
    assert token.text == "hi", "Token text was not stored correctly."
    assert token.confidence == 0.9, "Token confidence was not stored correctly."
    assert token.is_confident(0.8) == True, "A token with 0.9 confidence should pass an 0.8 threshold."
    assert token.is_confident(0.95) == False, "A token with 0.9 confidence should fail an 0.95 threshold."
