
from utils.singleton import Singleton
from web.dao.campagne_dao import CampagneDAO
from web.dao.utilisateur_campagne_dao import UtilisateurCampagneDao


class CampagneService(metaclass = Singleton):

    @staticmethod    
    def sauvegarder(): 
        pass
    
    @staticmethod
    def est_une_campagne(id : str,nom : str):
        if CampagneDAO.get_campagne(id)[1] == nom :
            return True
        return False
    
    def add_util_campagne(nom_util,id_camp,joueur):
        if nom_util in CampagneDAO.trouve_joueurs(id_camp):
            return UtilisateurCampagneDao.add_utilisateur_campagne(nom_util,id_camp,joueur)

    def liste_id():
        return CampagneDAO.liste_id()

    def get_campagne(id_campagne):
        return CampagneDAO.get_campagne(id_campagne)

    def trouve_mj(id_campagne):
        return CampagneDAO.trouve_mj(id_campagne)

    def trouve_joueurs(id_campagne):
        return CampagneDAO.trouve_joueurs(id_campagne) 

    def mettre_joueur_dans_campagne(username):
        return CampagneDAO.mettre_joueur_dans_campagne(username)    

    def retirer_joueur_de_campagne(username):
        return CampagneDAO.retirer_joueur_de_campagne(username)   
 
    @staticmethod
    def dict_campagnes():
        return CampagneDAO.dict_campagnes()  

         

