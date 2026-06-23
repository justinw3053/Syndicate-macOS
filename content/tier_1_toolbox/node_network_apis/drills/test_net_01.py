import pytest
import active_lab
from unittest.mock import patch, MagicMock

def test_http_get():
    mock_resp = MagicMock()
    mock_resp.read.return_value = b"OK"
    
    with patch("urllib.request.urlopen", return_value=mock_resp):
        assert active_lab.perform_http_get("http://dummy.url") == "OK"
