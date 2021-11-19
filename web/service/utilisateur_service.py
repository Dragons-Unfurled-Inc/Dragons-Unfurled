import hashlib
from getpass import getpass

from objets_metier.joueur import Joueur
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO


class UtilisateurService:
    """
    Cette classe fournit les services de création et de suppression
    de comptes aux utilisateurs, mais aussi de connexion et de deconnexion.
    """

    @staticmethod
    def noms_utilisateurs(): 
        return UtilisateurDAO.liste_noms() 

    @staticmethod
    def creation_compte(identifiant, mot_de_passe, est_admin):         
        UtilisateurDAO.createUtilisateur(identifiant, mot_de_passe, est_admin)

    @staticmethod
    def verifie_mdp(utilisateur_nom: str, mdp):
        return UtilisateurDAO.verifie_mdp(utilisateur_nom, mdp)

    @staticmethod
    def utilisateur_admin(utilisateur_nom: str):
        return UtilisateurDAO.getUtilisateurAdmin(utilisateur_nom)

    @staticmethod
    def est_utilisateur(nom: str):
        return UtilisateurDAO.getUtilisateur(nom)

    def trouver_perso(id_campagne : int, id_joueur : int):
        return UtilisateurDAO.trouver_perso(id_campagne, id_joueur)