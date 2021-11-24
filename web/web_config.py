import os
from utils.singleton import Singleton
import requests

class WebConfig(metaclass=Singleton):
    def __init__(self) -> None:
        from dotenv import load_dotenv
        load_dotenv()
        api_url=os.environ['API_URL']
        output_dir=os.environ['FILE_OUTPUT_DIR']
        dnd_url=os.environ['DND_URL']
        graph_port=os.environ['GRAPH_URL']
        self.dnd_port=dnd_url
        self.graph_port=graph_port
        self.api_port=api_url
        self.output_dir=output_dir
        
        
    def getApiPort(self) -> str:
        return str(self.api_url)
    
    def getDNDPort(self) -> str:
        return str(self.dnd_url)
    
    def getGraphPort(self) -> str:
        return str(self.graph_port)
    
    def getdnd(self,req:str):
        url = str.format("{0}/{1}",self.dnd_port,req)
        return requests.get(url).json()
    
    def post(self,query):
        return requests.post(self.graph_port,json={"query":query})
        