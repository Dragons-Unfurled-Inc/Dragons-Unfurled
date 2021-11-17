from typing import List

from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.feedback import FeedBack
from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.campagne_dao import CampagneDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.utilisateur_dao import UtilisateurDAO


class MaitreDuJeuService(metaclass = Singleton):

    @staticmethod    
    def ajouter_entite(identifiant_entite): 
        pass

    @staticmethod    
    def supprimer_entite(identifiant_entite): 
        pass

    @staticmethod    
    def trouve_entite(identifiant_entite): 
        pass

    @staticmethod
    def creer_campagne(nom_campagne: str): 
        CampagneDAO.creer_campagne(nom_campagne) 
