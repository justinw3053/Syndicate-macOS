import pytest
import active_lab
from unittest.mock import patch, MagicMock
import urllib.error

def test_status_code():
    mock_resp = MagicMock()
    mock_resp.status = 200
    
    with patch("urllib.request.urlopen", return_value=mock_resp):
        assert active_lab.get_http_status_code("http://dummy.url") == 200
        
    mock_error = urllib.error.HTTPError("http://dummy.url", 404, "Not Found", {}, None)
    with patch("urllib.request.urlopen", side_effect=mock_error):
        assert active_lab.get_http_status_code("http://dummy.url") == 404
