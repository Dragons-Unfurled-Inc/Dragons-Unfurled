
from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException
from psycopg2.extensions import register_adapter, AsIs
from pydantic import SecretBytes

# def adapt_pydantic_byte(Byte):
#         return AsIs(repr(Byte))

# register_adapter(SecretBytes, adapt_pydantic_byte)

class UtilisateurDAO:

    @staticmethod
    def liste_noms():
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT username "\
                    "FROM utilisateur"
                )
                res = cursor.fetchone()
        return res["username"]

    @staticmethod
    def verifie_mdp(utilisateur_nom: str, password: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM utilisateur "\
                    "WHERE utilisateur.username=%(nom)s and utilisateur.password=%(mdp)s"\
                    ,{"nom" : utilisateur_nom,"mdp":password}
                )
                res = cursor.fetchone()
            if res != None:
                return True
            return False

    @staticmethod
    def getUtilisateur(utilisateur_nom: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Utilisateur "\
                    "WHERE username=%(nom)s"\
                    ,{"nom" : utilisateur_nom}
                )
                res = cursor.fetchone()
        if res:
            return True
        else : 
            return False

    @staticmethod
    def getUtilisateurAdmin(utilisateur_nom: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Utilisateur "\
                    "WHERE username=%(nom)s and est_administrateur = True"\
                    ,{"nom" : utilisateur_nom}
                )
                res = cursor.fetchone()
        if res:
            return True
        else : 
            return False

    @staticmethod
    def createUtilisateur(identifiant,mot_de_passe,est_admin) -> Utilisateur:
        if UtilisateurDAO.getUtilisateur(identifiant) :
            print('Cet utilisateur existe déjà')
        else :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Utilisateur (username, "\
                                                    "est_administrateur, "\
                                                    "password) "\
                            "VALUES "\
                            "(%(username)s,%(est_administrateur)s, %(password)s);", 
                            { "username" : identifiant
                            , "est_administrateur": est_admin
                            , "password": mot_de_passe}
                        )
            
            print("Votre compte a été créé avec succès !")
            

    @staticmethod
    def updateUtilisateur(utilisateur_nom: str, utilisateur: Utilisateur) -> Utilisateur:
        utilisateur_to_update: Utilisateur = UtilisateurDAO.getUtilisateur(utilisateur_nom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE utilisateur SET utilisateur_nom=%(identifiant)s, password=%(password)s where id_utilisateur=%(id_utilisateur)s;", {"id_utilisateur": utilisateur_to_update.id, "utilisateur_nom": utilisateur.utilisateur_nom, "password": utilisateur.password})
