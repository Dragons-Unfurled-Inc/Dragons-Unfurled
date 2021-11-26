from client.exceptions.entite_introuvable_exception import EntiteIntrouvableException
from web.dao.entite_dao import EntiteDAO

from objets_metier.entite import Entite

from utils.singleton import Singleton

class Recherche(metaclass = Singleton):


    @staticmethod    
    def modifie_pv(entite: Entite, dommage: int):
        id_entite = entite.id_entite
        if entite.caracteristiques_entite.vie > dommage:
            EntiteDAO.diminution_pv(id_entite, dommage)
        else:
            EntiteDAO.tuer(id_entite)