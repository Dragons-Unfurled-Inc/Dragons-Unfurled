from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO

class UtilisateurService() :

    @staticmethod
    def add_utilisateur(utilisateur : Utilisateur):
        UtilisateurDAO.createUtilisateur(utilisateur)
        