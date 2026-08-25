import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from API_server.api_server import app

client = TestClient(app)

def test_api_health():
    response = client.get("/health")
    data = response.json()
    assert response.status_code == 200
    assert data == {"status": "ok"}
    