import pytest
import ex_bpe_03 as active_lab

def test_merge_pair():
    corpus = [["h", "u", "g"], ["p", "u", "g"]]
    new_corpus = active_lab.merge_pair(("u", "g"), corpus)
    assert new_corpus == [["h", "ug"], ["p", "ug"]], "Failed to merge the pair"
