from client.web_client.monstre_client import MonstreClient


class MonstreService():
    
    @staticmethod
    def ImportMonstreWeb(nom = str):
        return MonstreClient.ImportMonstreWeb(nom)
        
    @staticmethod
    def ImportMonstreParType(type):
        return MonstreClient.ImportMonstreParType(type)
    
    @staticmethod
    def ImportListeTypes():
        return MonstreClient.ImportListeTypes()
