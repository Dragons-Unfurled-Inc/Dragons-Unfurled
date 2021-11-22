
from utils.singleton import Singleton
from web.dao.entite_dao import EntiteDAO


class JoueurService(metaclass = Singleton):
  
    @staticmethod    
    def consulter_entites(): 
        return EntiteDAO.obtenir_entites_noms_id_joueur()
