from web.dao.db_connection import DBConnection
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO

class AdministrateurDAO:

    @staticmethod
    def supprimer_compte(utilisateur_nom: str) -> Utilisateur:
        utilisateur_a_supprimer: Utilisateur = UtilisateurDAO.getUtilisateur(utilisateur_nom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Utilisateur "\
                    "WHERE username = %(utilisateur_nom)s;"\
                    , {"utilisateur_nom": utilisateur_a_supprimer.identifiant})

    @staticmethod
    def ajouter_droits_administrateur(utilisateur: Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Utilisateur "\
                    "SET est_administrateur = %(est_administreurs)s"\
                    "WHERE username = %(utilisateur_nom)s;"\
                    , {"est_administrateur" : True
                    , "utilisateur_nom": utilisateur.identifiant})

    @staticmethod
    def supprimer_droits_administrateur(utilisateur: Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Utilisateur "\
                    "SET est_administrateur = %(est_administreurs)s"\
                    "WHERE username = %(utilisateur_nom)s;"\
                    , {"est_administrateur" : False
                    , "utilisateur_nom": utilisateur.identifiant})