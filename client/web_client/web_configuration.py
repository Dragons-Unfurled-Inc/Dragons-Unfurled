import os

import requests
from utils.singleton import Singleton


class WebConfiguration(metaclass=Singleton):
    """
    Classe technique pour se connecter à la base de données
    """

    def __init__(self):
        from dotenv import load_dotenv
        load_dotenv()
        # Open the connection.
        self.api_url = os.environ['API_URL']
        self.output_dir = os.environ['FILE_OUTPUT_DIR']

    # @property
    # def connection(self):
    #     return the opened connection.
    #     return self.__connection

    def getApiUrl(self):
        return self.api_url
    
    def getOutputDir(self):
        return self.output_dir

    def get(self,req:str):
        url = str.format("{0}/{1}",self.api_url,req)
        return requests.get(url).json()
        