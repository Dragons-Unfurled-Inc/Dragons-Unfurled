import requests as req
from web.dao.monstre_dao import MonstreDAO 
from objets_metier.monstre import Monstre
class MonstreService():
    

    @staticmethod
    def ImportMonstreWeb(nom = str):
        req = MonstreDAO.web_monstre(nom)
        return Monstre.parse_obj(req.json())
        