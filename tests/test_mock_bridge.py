from unittest.mock import patch
import pytest
import os
import json
from backend.main import create_app

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_api_track_endpoint(client, tmp_path):
    # Test that the backend endpoint exists and handles progress updates
    test_path = tmp_path / "memory.txt"
    with patch('backend.state_manager.MEMORY_PATH', str(test_path)):
        response = client.post('/api/track', json={"lesson": "Mission 1, Lesson 1"})
        assert response.status_code == 200
        
        # Verify it wrote to disk
        assert os.path.exists(test_path)
        with open(test_path, 'r') as f:
            content = f.read()
            assert "Mission 1, Lesson 1" in content

