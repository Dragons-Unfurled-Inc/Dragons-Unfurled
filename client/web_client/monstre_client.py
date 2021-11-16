import requests as requ
from objets_metier.caracteristique import Caracteristique
from web.dao.monstre_dao import MonstreDAO 
from objets_metier.monstre import Monstre
from client.web_client.web_configuration import WebConfiguration

class MonstreClient():
    
        @staticmethod
        def ImportMonstreWeb(nom = str):
            configuration = WebConfiguration()
            api_url = configuration.getApiUrl()
            api_dest = str.format("{}/monstre/{}",api_url,nom)
            d = requ.get(api_dest)
            return (Monstre(d["type"],0,0,Caracteristique(d['name'],d['actions'],d['senses'],d['languages'],d['special_abilities']+d['legendary_actions'],'')))
            
    
        @staticmethod
        def ImportMonstreParType(triche = bool):
            pass
        
        @staticmethod
        def ImportListeTypes():
            pass
            