from utils.singleton import Singleton
import os

class WebConfig(metaclass=Singleton):
    def __init__(self) -> None:
        api_port="localhost:5000"
        output_dir="./generated/"
        self.api_port=api_port
        self.output_dir=output_dir
        
    def getApiPort(self) -> str:
        return str(self.api_port)
    