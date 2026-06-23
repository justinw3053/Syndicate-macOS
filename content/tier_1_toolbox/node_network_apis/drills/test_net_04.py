import pytest
import active_lab
from unittest.mock import patch
import socket

def test_timeout():
    with patch("urllib.request.urlopen", side_effect=socket.timeout):
        assert active_lab.perform_get_with_timeout("http://dummy.url", 1.0) == "timeout_exceeded"
