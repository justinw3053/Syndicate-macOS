import pytest
import active_lab
import os

def test_resolve_path(tmp_path):
    base = os.path.join(tmp_path, "sub_folder")
    path = active_lab.resolve_and_create_path(base, "log.json")
    
    assert os.path.exists(base)
    assert path == os.path.join(base, "log.json")
