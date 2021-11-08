import requests as req
from objets_metier.caracteristique import Caracteristique
from web.dao.monstre_dao import MonstreDAO 
from objets_metier.monstre import Monstre
class MonstreService():
    

    @staticmethod
    def ImportMonstreWeb(nom = str):
        req = MonstreDAO.web_monstre(nom)
        d=req.json()
        #return(d)
        return (Monstre(d["type"],0,0,Caracteristique(d['name'],d['actions'],d['senses'],d['languages'],d['special_abilities']+d['legendary_actions'],'')))
        