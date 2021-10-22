from objets_metier.utilisateur.user import User
from dao.configuration import DBConnection
from exceptions.user_not_found_exception import UserNotFoundException


class UserDao:

    @staticmethod
    def verifyPassword(username: str, password: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM user where user.username=%(username)s and user.password=%(password)s"
                )
                res = cursor.fetchone()
            if res["username"] != None:
                return True
            return False

    @staticmethod
    def getUser(username: str) -> User:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM user where user.username=%(username)s"
                )
                res = cursor.fetchone()
        if res:
            return User(id=res["id_user"], username=res["username"], password=res["password"])
        else:
            raise UserNotFoundException(username)

    @staticmethod
    def createUser(user: User) -> User:
        try:
            UserDao.getUser(user.username)
        except UserNotFoundException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO user (id,username, password), VALUES "
                        "(%(id_type)s, %(name)s);", {"username": user.username, "password": user.password})
            return UserDao.getUser(user.username)

    @staticmethod
    def updateUser(username: str, user: User) -> User:
        user_to_update: User = UserDao.getUser(username)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE user SET username=%(username)s, password=%(password)s where id_user=%(id_user)s;", {"id_user": user_to_update.id, "username": user.username, "password": user.password})

    @staticmethod
    def deleteUser(username: str) -> User:
        user_to_delete: User = UserDao.getUser(username)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Delete from user where id_user=%(username)s;", {"username": user_to_delete.id})
