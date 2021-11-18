from typing import List

from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.feedback import FeedBack
from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.campagne_dao import CampagneDAO
from web.dao.donjon_dao import DonjonDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO
from web.dao.utilisateur_dao import UtilisateurDAO


class MaitreDuJeuService(metaclass = Singleton):
  
    @staticmethod    
    def ajouter_entite_campagne(identifiant_entite): 
        EntiteDAO.ajouter_entite_campagne(identifiant_entite)

    @staticmethod    
    def supprimer_entite(identifiant_entite): 
        pass

    @staticmethod    
    def trouve_entite(identifiant_entite): 
        pass

    @staticmethod
    def creer_campagne(nom_campagne: str): 
        CampagneDAO.creer_campagne(nom_campagne) 

    @staticmethod
    def voir_les_donjons():
        print("Voici l'ensemble des donjons, ainsi que leurs contenus :")
        donjons = MaitreDuJeuDAO.donjons()
        for donjon in donjons:
            print(donjon)
