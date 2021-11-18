import os

from utils.singleton import Singleton


class WebConfig(metaclass=Singleton):
    def __init__(self) -> None:
        from dotenv import load_dotenv
        load_dotenv()
        api_port=os.environ['API_URL']
        output_dir=os.environ['FILE_OUTPUT_DIR']
        self.api_port=api_port
        self.output_dir=output_dir
        
        
    def getApiPort(self) -> str:
        return str(self.api_port)
    