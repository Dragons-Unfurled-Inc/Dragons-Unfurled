from utils.singleton import Singleton
from web.dao.objet_dao import ObjetDAO


class ObjetService(metaclass = Singleton):

    @staticmethod
    def ramasse_objet(identifiant_entite: int, identifiant_objet: int):
        ObjetDAO.ramasse_entite_objet(identifiant_entite, identifiant_objet) 
