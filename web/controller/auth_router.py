from fastapi import APIRouter
from objets_metier.user import User
from service.user_service import UserService

router = APIRouter()


@router.post("/users/", tags=["users"])
def create_user(user: User):
    return UserService.createUser(user)


@router.put("/users/{user_name}", tags=["users"])
def update_user(user_name: str, user: User):
    return UserService.updateUser(user_name, user)


@router.get("/users/{user_name}", tags=["users"])
def get_user(user_name: str):
    return UserService.getUser(user_name)
