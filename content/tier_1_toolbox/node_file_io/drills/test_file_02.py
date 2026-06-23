import pytest
import active_lab
import os

def test_write_file(tmp_path):
    path = os.path.join(tmp_path, "log.txt")
    active_lab.write_telemetry_file(path, "status: ok")
    
    with open(path, "r") as f:
        assert f.read() == "status: ok"
