import os

import psycopg2.extras
from utils.singleton import Singleton


class WebConfiguration(metaclass=Singleton):
    """
    Classe technique pour se connecter à la base de données
    """

    def __init__(self):
        # Open the connection.
        self.api_url = "localhost:5000"
        self.output_dir = "./generated/"

    # @property
    # def connection(self):
    #     return the opened connection.
    #     return self.__connection

    def getApiUrl(self):
        return self.api_url
    
    def getOutputDir(self):
        return self.output_dir
