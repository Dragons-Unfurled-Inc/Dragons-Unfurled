from typing import List

from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.feedback import FeedBack
from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.campagne_dao import CampagneDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.utilisateur_campagne_dao import UtilisateurCampagneDao
from web.dao.utilisateur_dao import UtilisateurDAO


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

