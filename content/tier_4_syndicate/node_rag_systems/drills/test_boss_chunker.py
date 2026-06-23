import pytest
import active_lab

def test_chunker():
    text = "A B C D E F G H I"
    # Overlap of 1 word, chunk size of 3 words
    chunks = active_lab.chunk_text(text, 3, 1)
    # Expected:
    # "A B C"
    # "C D E"
    # "E F G"
    # "G H I"
    assert chunks == ["A B C", "C D E", "E F G", "G H I"]
