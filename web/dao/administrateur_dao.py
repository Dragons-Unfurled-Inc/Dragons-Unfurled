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
                    "Delete from utilisateur where id_utilisateur=%(utilisateur_nom)s;", {"utilisateur_nom": utilisateur_a_supprimer.id})

    @staticmethod
    def ajouter_droits_administrateur(utilisateur: Utilisateur):
        return []

    @staticmethod
    def supprimer_droits_administrateur(utilisateur: Utilisateur):
        return []