import pytest
import active_lab
def test_shared_state_bug():
    chat_a = active_lab.Conversation('You are a helpful assistant.')
    chat_a.add_user_message('Hello AI.')
    chat_b = active_lab.Conversation('You are a strict code reviewer.')
    chat_b.add_user_message('Review this script.')
    assert len(chat_a.messages) == 2, f'chat_a leaked state: {chat_a.messages}'
    assert len(chat_b.messages) == 2, f'chat_b leaked state: {chat_b.messages}'
