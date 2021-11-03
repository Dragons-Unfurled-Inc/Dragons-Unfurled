from typing import List

from utils.singleton import Singleton
from objets_metier.feedback import Feedback
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO
from web.dao.feed_back_dao import FeedBackDAO
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class AdministrateurService(metaclass = Singleton):

    @staticmethod    
    def bannir(self, nom_utilisateur: str):
        if nom_utilisateur in UtilisateurDAO.liste_noms(): # Nous vérifions si ce nom d'utilisateur existe.
            UtilisateurDAO.SupprimerCompte(nom_utilisateur)
        else:
            raise UtilisateurIntrouvableException(nom_utilisateur)
    
    @staticmethod
    def consulter_feed_back_admin(self):
        FeedbackDAO.consulter_tous()

    @staticmethod
    def donner_droits_admin(self, nom_utilisateur: str):
        None