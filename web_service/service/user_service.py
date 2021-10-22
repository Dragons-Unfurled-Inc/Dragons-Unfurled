from app.web_service.exception.user_not_authenticated_exception import UserNotAuthenticated
from objets_metiers.utilisateur.user import User
from app.web_service.dao.user_dao import UserDao


class UserService:

    @staticmethod
    def createUser(user: User) -> User:
        return UserDao.createUser(user)

    @staticmethod
    def getUser(user_name: str) -> User:
        return UserDao.getUser(user_name)

    @staticmethod
    def updateUser(user_name: str, user: User) -> User:
        return UserDao.updateUser(user_name, user)

    @staticmethod
    def deleteUser(user_name: str) -> User:
        return UserDao.deleteUser(user_name)

    @staticmethod
    def authenticate_and_get_user(username: str, password: str) -> User:
        if (UserDao.verifyPassword(username, password)):
            return UserDao.getUser(username)
        else:
            raise UserNotAuthenticated(username=username)
