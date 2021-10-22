
from app.business_object.user import User



class UserService:

    @staticmethod
    def createUser(user: User) -> User:
        return UserDao.createUser(user)

    @staticmethod
    def authenticate_and_get_user(username: str, password: str) -> User:
        if (UserDao.verifyPassword(username, password)):
            return UserDao.getUser(username)
        else:
            raise UserNotAuthenticated(username=username)
