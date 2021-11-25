import os

import psycopg2.extras
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
        api_url=os.environ['API_URL']
        output_dir=os.environ['FILE_OUTPUT_DIR']
        dnd_url=os.environ['DND_URL']
        graph_port=os.environ['GRAPH_URL']
        self.dnd_port=dnd_url
        self.graph_port=graph_port
        self.api_url=api_url
        self.output_dir=output_dir
        
    # @property
    # def connection(self):
    #     return the opened connection.
    #     return self.__connection

    def getApiUrl(self):
        return self.api_url
    
    def getOutputDir(self):
        return self.output_dir

    def get(self,req:str):
        url = str.format("http://{0}/{1}",self.api_url,req)
        return requests.get(url).json()
        