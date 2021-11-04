from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class MjDAO:

    @staticmethod
    def personnages_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso joueurs 
        return []

    @staticmethod
    def personnages_non_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso non joueurs 
        return []

    @staticmethod
    def monstres(id_campagne):# Cette fonction renvoie l'ensemble des pmonstres 
        return []

    @staticmethod
    def donjons(id_campagne):# Cette fonction renvoie l'ensemble des donjons
        return []            
