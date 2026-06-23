import pytest
import active_lab
def test_get_stats():
    corpus = [['h', 'u', 'g', '</w>'], ['p', 'u', 'g', '</w>']]
    stats = active_lab.get_stats(corpus)
    assert stats[('u', 'g')] == 2
    assert stats[('h', 'u')] == 1
