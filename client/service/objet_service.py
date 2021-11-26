from client.web_client.objet_client import ObjetClient
from web.dao.objet_dao import ObjetDAO

from utils.singleton import Singleton

class ObjetService(metaclass = Singleton):

    @staticmethod
    def ramasse_objet(identifiant_entite: int, identifiant_objet: int):
        ObjetDAO.ramasse_entite_objet(identifiant_entite, identifiant_objet) 

    @staticmethod
    def ImportObjetWeb(nom = str):
        return ObjetClient.ImportObjetWeb(nom)
        
    @staticmethod
    def ImportObjetDeType(type):
        return ObjetClient.ListeObjetsDeType(type)
    
    @staticmethod
    def ImportListeTypes():
        return ObjetClient.ListeTypesObjet()
    
    # @staticmethod
    # def ImportListeTypes():
    #     return ObjetClient.ListeTypesObjet()