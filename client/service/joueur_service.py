
from utils.singleton import Singleton
from web.dao.entite_dao import EntiteDAO
from web.dao.campagne_dao import CampagneDAO


class JoueurService(metaclass = Singleton):
  
    @staticmethod    
    def consulter_entites(): 
        return EntiteDAO.obtenir_entites_noms_id_joueur()

    @staticmethod    
    def trouve_entite_campagne(): 
        return CampagneDAO.trouve_entite_campagne_joueur() 
