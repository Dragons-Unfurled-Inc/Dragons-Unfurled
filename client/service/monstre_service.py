import requests as requ
from objets_metier.caracteristique import Caracteristique
from web.dao.monstre_dao import MonstreDAO 
from objets_metier.monstre import Monstre
class MonstreService():
    

    @staticmethod
    def ImportMonstreWeb(nom = str):
        req = requ.get('https://www.dnd5eapi.co/api/monsters/' + nom)
        d=req.json()
        return (Monstre(d["type"],0,0,Caracteristique(d['name'],d['actions'],d['senses'],d['languages'],d['special_abilities']+d['legendary_actions'],'')))
        