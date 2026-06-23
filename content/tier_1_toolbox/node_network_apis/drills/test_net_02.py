import pytest
import active_lab
from unittest.mock import patch, MagicMock

def test_http_post():
    mock_resp = MagicMock()
    mock_resp.read.return_value = b'{"success": true}'
    
    with patch("urllib.request.urlopen", return_value=mock_resp):
        res = active_lab.perform_http_post("http://dummy.url", {"test": 1})
        assert "success" in res
