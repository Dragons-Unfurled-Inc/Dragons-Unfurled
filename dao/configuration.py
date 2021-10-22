import os

import psycopg2
from psycopg2.extras import RealDictCursor
from app.utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """

    def __init__(self):
        # Open the connection.
        self.__connection = psycopg2.connect(
            host=os.environ["PG_HOST"],
            port=os.environ["PG_PORT"],
            database=os.environ["PG_DATABASE"],
            user=os.environ["PG_USER"],
            password=os.environ["PG_PASSWORD"],
            cursor_factory=RealDictCursor)

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection
