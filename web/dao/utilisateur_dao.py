from objets_metier.utilisateur import Utilisateur
from dao.configuration import DBConnection
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class UtilisateurDao:

    @staticmethod
    def verifie_mdp(utilisateur_nom: str, password: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM utilisateur where utilisateur.utilisateur_nom=%(utilisateur_nom)s and utilisateur.password=%(password)s"
                )
                res = cursor.fetchone()
            if res["utilisateur_nom"] != None:
                return True
            return False

    @staticmethod
    def getUtilisateur(utilisateur_nom: str) -> Utilisateur:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM utilisateur where utilisateur.utilisateur_nom=%(utilisateur_nom)s"
                )
                res = cursor.fetchone()
        if res:
            return Utilisateur(id=res["id_utilisateur"], utilisateur_nom=res["utilisateur_nom"], password=res["password"])
        else:
            raise UtilisateurIntrouvableException(utilisateur_nom)

    @staticmethod
    def createUtilisateur(utilisateur: Utilisateur) -> Utilisateur:
        try:
            UtilisateurDao.getUtilisateur(utilisateur.utilisateur_nom)
        except UtilisateurIntrouvableException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO utilisateur (id,utilisateur_nom, password), VALUES "
                        "(%(id_type)s, %(name)s);", {"utilisateur_nom": utilisateur.utilisateur_nom, "password": utilisateur.password})
            return UtilisateurDao.getUtilisateur(utilisateur.utilisateur_nom)

    @staticmethod
    def updateUtilisateur(utilisateur_nom: str, utilisateur: Utilisateur) -> Utilisateur:
        utilisateur_to_update: Utilisateur = UtilisateurDao.getUtilisateur(utilisateur_nom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE utilisateur SET utilisateur_nom=%(utilisateur_nom)s, password=%(password)s where id_utilisateur=%(id_utilisateur)s;", {"id_utilisateur": utilisateur_to_update.id, "utilisateur_nom": utilisateur.utilisateur_nom, "password": utilisateur.password})

    @staticmethod
    def deleteUtilisateur(utilisateur_nom: str) -> Utilisateur:
        utilisateur_to_delete: Utilisateur = UtilisateurDao.getUtilisateur(utilisateur_nom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Delete from utilisateur where id_utilisateur=%(utilisateur_nom)s;", {"utilisateur_nom": utilisateur_to_delete.id})