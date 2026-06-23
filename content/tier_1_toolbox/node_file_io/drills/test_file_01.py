import pytest
import active_lab
import os

def test_read_file(tmp_path):
    path = os.path.join(tmp_path, "test.txt")
    with open(path, "w") as f:
        f.write("Hello World")
        
    assert active_lab.read_text_file(path) == "Hello World"
