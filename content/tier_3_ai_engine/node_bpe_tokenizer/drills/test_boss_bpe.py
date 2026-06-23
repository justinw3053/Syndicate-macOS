import pytest
import boss_bpe as active_lab

def test_train_bpe():
    corpus = [["l", "o", "w"], ["l", "o", "w", "e", "s", "t"], ["n", "e", "w", "e", "r"]]
    merged = active_lab.train_bpe(corpus, 2)
    assert sum(len(word) for word in merged) < 14, "The corpus was not merged properly."
