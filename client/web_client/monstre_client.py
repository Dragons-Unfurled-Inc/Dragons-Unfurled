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
            api_dest = str.format("http://{}/monstre/{}",api_url,nom)
            # http://localhost:5000/monstre/zombie
            # localhost:5000/monstre/zombie
            d = requ.get(api_dest)
            d = d.json()
            print(d)
            return (Monstre(type = d["type"],id_joueur = d['id_joueur'],id_entite = d['id_entite'],caracteristiques_entite = Caracteristique(nom_entite = d['caracteristiques_entite']['nom_entite'])))
            
    
        @staticmethod
        def ImportMonstreParType(triche = bool):
            pass
        
        @staticmethod
        def ImportListeTypes():
            pass
            