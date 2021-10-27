from dao.utilisateur_dao import UtilisateurDao
from objets_metier.utilisateur import Utilisateur
from exceptions.utilisateur_non_authentifie_exception import UtilisateurNonAuthentifie

class UtilisateurService:

    @staticmethod
    def createutilisateur(utilisateur: Utilisateur) -> Utilisateur:
        return UtilisateurDao.createutilisateur(utilisateur)

    @staticmethod
    def authenticate_and_get_utilisateur(utilisateur_nom: str, password: str) -> Utilisateur:
        if (UtilisateurDao.verifyPassword(utilisateur_nom, password)):
            return UtilisateurDao.getutilisateur(utilisateur_nom)
        else:
            raise UtilisateurNonAuthentifie(utilisateur_nom=utilisateur_nom)
