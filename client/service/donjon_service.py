from typing import List

from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.donjon import Donjon
from objets_metier.feedback import FeedBack
from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.donjon_dao import DonjonDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO
from web.dao.salle_dao import SalleDAO
from web.dao.utilisateur_dao import UtilisateurDAO


class DonjonService(metaclass = Singleton):

    @staticmethod
    def construire_donjon(nom_donjon: str, coordonnees_salle_donjon_x: int, coordonnees_salle_donjon_y: int):
       DonjonDAO.ajoute_donjon(nom_donjon, coordonnees_salle_donjon_x, coordonnees_salle_donjon_y)

    @staticmethod
    def editer_donjon(self, donjon : Donjon): 
       None      

    @staticmethod
    def dict_donjons():
        return DonjonDAO.dict_donjons()

    @staticmethod
    def existe_donjon_campagne(id_donjon: int):
        return DonjonDAO.existe_donjon_campagne(id_donjon)

    @staticmethod
    def existe_entite_campagne(id_entite: int):
        return EntiteDAO.existe_entite_campagne(id_entite)

    @staticmethod
    def existe_salle_donjon(id_salle: int):
        return DonjonDAO.existe_salle_donjon(id_salle)

    @staticmethod
    def espace_libre_salle(x: int, y: int): 
       return DonjonDAO.espace_libre_salle(x,y) 

    @staticmethod
    def ajouter_entite_salle(identifiant_entite: int, identifiant_salle: int): 
        return SalleDAO.ajouter_entite_salle(identifiant_entite, identifiant_salle) 

    @staticmethod
    def ajouter_entites_salle(identifiant_salle: int): 
        dictionnaire = MaitreDuJeuDAO.dict_entites()
        for entite in dictionnaire:
            SalleDAO.ajouter_entite_salle(entite["id_entite"], identifiant_salle)
