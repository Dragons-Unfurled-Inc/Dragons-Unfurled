from typing import List

from utils.singleton import Singleton
from objets_metier.feedback import Feedback
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.feed_back_dao import FeedBackDAO
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class DonjonService(metaclass = Singleton):

    @staticmethod    
    def creation_donjon(nom_donjon): 
        pass