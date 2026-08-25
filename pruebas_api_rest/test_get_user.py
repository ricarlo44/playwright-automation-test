import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from API_server.api_server import app

client = TestClient(app)


def test_user_validation():
   response = client.get("/users/1")
   data = response.json()

   assert response.status_code == 200
   assert isinstance(data["id"], int)
   # support both legacy 'username' key and current 'name' key
   user_name = data.get("name") or data.get("username")
   assert isinstance(user_name, str)

   assert "email" in data
   assert "@" in data["email"]


def test_user_validation_not_found():
   response = client.get("/users/0")

   assert response.status_code == 404
   assert "detail" in response.json()
   assert response.json()["detail"] == "Usuario no encontrado"