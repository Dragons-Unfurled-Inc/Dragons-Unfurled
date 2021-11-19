
from typing import Any
from objets_metier.utilisateur import Utilisateur
from objets_metier.caracteristique import Caracteristique
from objets_metier.personnage import Personnage
from objets_metier.objet import Objet
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
    def verifie_mdp(utilisateur_nom: str, password: Any) -> bool:
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
        if res != None:
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

    @staticmethod
    def trouver_perso(id_campagne : int, id_joueur : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_joueur = %(id_joueur)s"\
                    "AND id_campagne = %(id_campagne)s"
                    , {"id_joueur" : id_joueur
                    , "id_campagne" : id_campagne})
                entite = cursor.fetchone()
                id_entite = entite["id_entite"]
                cursor.execute(
                    "SELECT *"\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                enti_obj = cursor.fetchall()
                liste_objet = []
                for i in [enti_obj[i]["id_objet"] for i in range(0, len(enti_obj))]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            perso = Personnage(personnage["classe"], personnage["race"], personnage["lore"],entite["id_joueur"], i, entite["nom_entite"], caract, liste_objet)
        return perso