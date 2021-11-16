from typing import List

from utils.singleton import Singleton
from objets_metier.feedback import Feedback
from objets_metier.utilisateur import Utilisateur
from web.dao.campagne_dao import CampagneDAO
from web.dao.utilisateur_campagne_dao import UtilisateurCampagneDao
from web.dao.utilisateur_dao import UtilisateurDAO
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.feed_back_dao import FeedBackDAO
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class CampagneService(metaclass = Singleton):

    @staticmethod    
    def sauvegarder(campagne): 
        pass
    
    @staticmethod
    def est_une_campagne(id : str,nom : str):
        if CampagneDAO.get_campagne(id)[1] == nom :
            return True
        return False
    
    def add_util_campagne(nom_util,id_camp,joueur):
        if nom_util in CampagneDAO.trouve_joueurs(id_camp):
            return UtilisateurCampagneDao.add_utilisateur_campagne(nom_util,id_camp,joueur)