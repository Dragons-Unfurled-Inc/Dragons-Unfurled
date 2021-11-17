import os

import psycopg2.extras
from utils.singleton import Singleton


class WebConfiguration(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """

    def __init__(self):
        # Open the connection.
<<<<<<< HEAD
        self.api_url = os.environ["API_URL"]
=======
        self._api_url = os.environ["API_URL"]
        self._output_dir = os.environ["FILE_OUTPUT_DIR"]
>>>>>>> 60bafacb5d2ae89bfa61f01c9569329b3cc30d92

    # @property
    # def connection(self):
    #     """
    #     return the opened connection.

<<<<<<< HEAD
        :return: the opened connection.
        """
        return self.connection
=======
    #     :return: the opened connection.
    #     """
    #     return self.__connection

    def getApiUrl(self):
        return self._api_url
    
    def getOutputDir(self):
        return self._output_dir
>>>>>>> 60bafacb5d2ae89bfa61f01c9569329b3cc30d92
