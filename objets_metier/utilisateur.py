from pydantic import BaseModel

class Utilisateur(BaseModel):
    id: int
    username: str
    password: str