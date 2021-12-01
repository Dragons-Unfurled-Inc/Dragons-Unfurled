from client.web_client.objet_client import ObjetClient
from utils.singleton import Singleton
from web.dao.objet_dao import ObjetDAO


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

    @staticmethod
    def trouve_id_obj(x,y, identifiant_salle):
        return ObjetDAO.trouve_id_obj(x,y, identifiant_salle)  

    @staticmethod
    def trouve_id_ent(x,y, identifiant_salle):
        return ObjetDAO.trouve_id_ent(x,y, identifiant_salle)  
    
    # @staticmethod
    # def ImportListeTypes():
    #     return ObjetClient.ListeTypesObjet()
