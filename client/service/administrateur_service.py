from typing import List

from utils.singleton import Singleton
from objets_metier.feedback import Feedback
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO
from web.dao.joueur_dao import JoueurDAO
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.feed_back_dao import FeedBackDAO
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class AdministrateurService(metaclass = Singleton):

    @staticmethod    
    def bannir(nom_utilisateur: str):
        if nom_utilisateur in JoueurDAO.liste_noms(): # Nous vérifions si ce nom d'utilisateur existe.
            AdministrateurDAO.supprimer_compte(nom_utilisateur)
        else:
            raise UtilisateurIntrouvableException(nom_utilisateur)

    @staticmethod
    def consulter_feed_back_admin():
        FeedBackDAO.consulter_tous()

    @staticmethod
    def transferer_droits_admin(nom_utilisateur: str, nom_administrateur_donneur: str):
        if nom_utilisateur in JoueurDAO.liste_noms(): # Nous vérifions si ce nom d'utilisateur existe et n'est pas déjà administrateur.
            AdministrateurDAO.ajouter_droits_administrateur(nom_utilisateur)
            AdministrateurDAO.supprimer_droits_administrateur(nom_administrateur_donneur)
        else:
            raise UtilisateurIntrouvableException(nom_utilisateur)