try:
    from pydantic import BaseModel
    from typing import Optional

    class User(BaseModel):
        id: Optional[int] = None
        name: str
        email: str
except Exception:
    class User:
        def __init__(self, id: int = None, name: str = "", email: str = ""):
            self.id = id
            self.name = name
            self.email = email
