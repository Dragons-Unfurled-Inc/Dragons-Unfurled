from utils.singleton import Singleton
import os

class WebConfig(metaclass=Singleton):
    def __init__(self) -> None:
        api_port=os.environ['API_URL']
        output_dir=os.environ['FILE_OUTPUT_DIR']
        self.api_port=api_port
        self.output_dir=output_dir
        
    def getApiPort(self) -> str:
        return str(self.api_port)
    