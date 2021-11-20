from typing import List

from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.feedback import FeedBack
from objets_metier.personnage import Personnage
from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.campagne_dao import CampagneDAO
from web.dao.donjon_dao import DonjonDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO
from web.dao.utilisateur_dao import UtilisateurDAO


class JoueurService(metaclass = Singleton):
  
    @staticmethod    
    def consulter_entites(): 
        return EntiteDAO.obtenir_entites_noms_id_joueur()
