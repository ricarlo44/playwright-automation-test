import json
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

try:
    from .model.user import User
except ImportError:
    from model.user import User

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "users.json")

def load_db():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)
    
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    users_db = load_db()
    user = next((u for u in users_db if u["id"] == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user

@app.post("/users/", status_code=201)
def create_user(user: User):
    users_db = load_db()
    if users_db:
        new_id = max(u["id"] for u in users_db) + 1
    else:
        new_id = 1

    user.id = new_id
    users_db.append(user.model_dump())

    with open(DATA_PATH, "w") as f:
        json.dump(users_db, f, indent=4)

    return {"message": "Usuario creado exitosamente", "user": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users_db = load_db()
    user = next((u for u in users_db if u["id"] == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    users_db = [u for u in users_db if u["id"] != user_id]

    with open(DATA_PATH, "w") as f:
        json.dump(users_db, f, indent=4)

    return {"message": "Usuario eliminado exitosamente", "user": user}

@app.post("/users/", status_code=201)
def create_user(user: User):
    users_db = load_db()
    if users_db:
        new_id = max(u["id"] for u in users_db) + 1
    else:
        new_id = 1

    user.id = new_id
    users_db.append(user.model_dump())

    with open(DATA_PATH, "w") as f:
        json.dump(users_db, f, indent=4)

    return {"message": "Usuario creado exitosamente", "user": user}
