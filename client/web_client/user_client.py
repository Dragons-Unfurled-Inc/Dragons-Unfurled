from exceptions.user_not_authenticated_exception import UserNotAuthenticated
from objets_metier.user import User
from dao.user_dao import UserDao
import requests
import os


class UserClient:

    @staticmethod
    def createUser(user: User) -> User:
        
        r = requests.get("http://localhost:5000")  

        return UserDao.createUser(user)

    @staticmethod
    def authenticate_and_get_user(username: str, password: str) -> User:
        if (UserDao.verifyPassword(username, password)):
            return UserDao.getUser(username)
        else:
            raise UserNotAuthenticated(username=username)
