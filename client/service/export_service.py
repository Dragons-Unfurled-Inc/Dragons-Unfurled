
from client.service.enregistrement_service import Enregistre
from client.web_client.export_client import ExportClient


class ExportService():
    
    @staticmethod
    def SauvegardeTable(table : str):
        donnees = ExportClient.SauvegardeTable(table)
        Enregistre.enregistrejson(donnees)
        
    def SauvegardeDB():
        donnees = ExportClient.SauvegardeDB()
        Enregistre.enregistrejson(donnees)
        
