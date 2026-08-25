import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from API_server.api_server import app

client = TestClient(app)


def test_create_user():
    new_user = {
        "name": "tester_pro",
        "email": "tester@example.com",
    }

    # Create user
    response = client.post("/users/", json=new_user)
    data_created_user = response.json()

    assert response.status_code == 201
    assert data_created_user["user"]["name"] == new_user["name"]

    created_user_id = data_created_user["user"]["id"]
    assert created_user_id is not None

    # Retrieve user
    response_get_user = client.get(f"/users/{created_user_id}")
    data_get_user = response_get_user.json()

    assert response_get_user.status_code == 200
    assert data_get_user["name"] == new_user["name"]

    # Delete user
    response_delete = client.delete(f"/users/{created_user_id}")
    assert response_delete.status_code == 200