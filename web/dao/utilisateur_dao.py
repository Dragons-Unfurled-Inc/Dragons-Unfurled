
from typing import Any

from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.personnage import Personnage
from objets_metier.monstre import Monstre
from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection

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
            return "Cet utilisateur existe déjà."
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
            
            return "Votre compte a été créé avec succès !"
            
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
                    "SELECT * "\
                    "FROM Entite "\
                    "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE username = %(username)s "\
                    "AND id_campagne = %(id_campagne)s "
                    , {"username" : id_joueur
                    , "id_campagne" : id_campagne})
                entite = cursor.fetchone()
                id_entite = entite["id_entite"]
                cursor.execute(
                    "SELECT * "\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT * "\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s "\
                    , {"id_entite" : id_entite})
                capacite = cursor.fetchall()
                if capacite == None : 
                    capacite = []
                else:
                    capacite = [capacite[i]["nom_capacite"] for i in range(len(capacite))]
                cursor.execute(
                    "SELECT * "\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                langage = cursor.fetchall()
                if langage == None:
                    langage =[]
                else:
                    langage = [langage[i]["nom_langage"] for i in range(len(langage))]
                cursor.execute(
                    "SELECT * "\
                    "FROM  Attaque "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                attaque = cursor.fetchall()
                if attaque == None :
                    attaque = []
                else : 
                    attaque = [attaque[i]["nom_attaque"] for i in range(0, len(attaque))]
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                enti_obj = cursor.fetchall()
                liste_objet = []
                for i in [enti_obj[i]["id_objet"] for i in range(0, len(enti_obj))]:
                    cursor.execute(
                    "SELECT * "\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchall()
                    if objet == None: 
                        objet = []
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = entite["description"], classe_armure = entite["classe_armure"])
            perso = Personnage(classe = personnage["classe"], race = personnage["race"], lore = personnage["lore"], id_joueur = entite["username"], id_entite = entite["id_entite"], nom_entite = entite["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet)
        return perso

    @staticmethod
    def trouver_perso_par_id(id_campagne : int, id_entite : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite "\
                    "WHERE id_entite = %(username)s "\
                    "AND id_campagne = %(id_campagne)s "
                    , {"username" : id_entite
                    , "id_campagne" : id_campagne})
                entite = cursor.fetchone()
                id_entite = entite["id_entite"]
                cursor.execute(
                    "SELECT * "\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT * "\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s "\
                    , {"id_entite" : id_entite})
                capacite = cursor.fetchall()
                if capacite == None : 
                    capacite = []
                else:
                    capacite = [capacite[i]["nom_capacite"] for i in range(len(capacite))]
                cursor.execute(
                    "SELECT * "\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                langage = cursor.fetchall()
                if langage == None:
                    langage =[]
                else:
                    langage = [langage[i]["nom_langage"] for i in range(len(langage))]
                cursor.execute(
                    "SELECT * "\
                    "FROM  Attaque "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                attaque = cursor.fetchall()
                if attaque == None :
                    attaque = []
                else : 
                    attaque = [attaque[i]["nom_attaque"] for i in range(0, len(attaque))]
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                enti_obj = cursor.fetchall()
                liste_objet = []
                for i in [enti_obj[i]["id_objet"] for i in range(0, len(enti_obj))]:
                    cursor.execute(
                    "SELECT * "\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchall()
                    if objet == None: 
                        objet = []
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = entite["description"], classe_armure = entite["classe_armure"])
            perso = Personnage(classe = personnage["classe"], race = personnage["race"], lore = personnage["lore"], id_joueur = -1, id_entite = entite["id_entite"], nom_entite = entite["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet)
        return perso    


    @staticmethod
    def trouver_monstre_par_id(id_campagne : int, id_entite : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite "\
                    "WHERE id_entite = %(username)s "\
                    "AND id_campagne = %(id_campagne)s "
                    , {"username" : id_entite
                    , "id_campagne" : id_campagne})
                entite = cursor.fetchone()
                id_entite = entite["id_entite"]
                cursor.execute(
                    "SELECT * "\
                    "FROM Monstre "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                monstre = cursor.fetchone()
                cursor.execute(
                    "SELECT * "\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s "\
                    , {"id_entite" : id_entite})
                capacite = cursor.fetchall()
                if capacite == None : 
                    capacite = []
                else:
                    capacite = [capacite[i]["nom_capacite"] for i in range(len(capacite))]
                cursor.execute(
                    "SELECT * "\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                langage = cursor.fetchall()
                if langage == None:
                    langage =[]
                else:
                    langage = [langage[i]["nom_langage"] for i in range(len(langage))]
                cursor.execute(
                    "SELECT * "\
                    "FROM  Attaque "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                attaque = cursor.fetchall()
                if attaque == None :
                    attaque = []
                else : 
                    attaque = [attaque[i]["nom_attaque"] for i in range(0, len(attaque))]
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                enti_obj = cursor.fetchall()
                liste_objet = []
                for i in [enti_obj[i]["id_objet"] for i in range(0, len(enti_obj))]:
                    cursor.execute(
                    "SELECT * "\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchall()
                    if objet == None: 
                        objet = []
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = entite["description"], classe_armure = entite["classe_armure"])
            mons = Monstre(type = monstre["type"] , id_joueur = -1, id_entite = entite["id_entite"], nom_entite = entite["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet)
        return mons