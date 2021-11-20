from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.caracteristique import Caracteristique
from objets_metier.donjon import Donjon
from objets_metier.monstre import Monstre
from objets_metier.objet import Objet
from objets_metier.personnage import Personnage
from objets_metier.salle import Salle
from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection
from client.vue.session import Session


class MaitreDuJeuDAO:
    
    @staticmethod
    def est_mj_campagne(id_campagne, id_joueur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_campagne, username "\
                    "FROM Utilisateur_Campagne "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND est_joueur = false"\
                    , {"id_campagne" : id_campagne})
                username = cursor.fetchone()
                username = username["username"]
        return id_joueur == username

    @staticmethod
    def existe_entite_nom_id_joueur(nom_entite, id_entite, id_joueur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE (Entite.id_entite = %(id_entite)s) "\
                    "AND (nom_entite = %(nom_entite)s) "\
                    "AND (username = %(username)s);"\
                    , {"id_entite" : id_entite
                    , "nom_entite" : nom_entite
                    , "username" : id_joueur })
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    @staticmethod
    def personnages_joueurs(id_campagne): 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_joueur <> %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : "-1"})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso_joueur = []
        for i in liste_entite: 
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                entite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                enti_obj = cursor.fetchone()
                liste_objet = []
                for i in enti_obj["id_objet"]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            liste_perso_joueur.append(Personnage(personnage["classe"], personnage["race"], personnage["lore"],entite["id_joueur"], i, entite["nom_entite"], caract, liste_objet))
        return liste_perso_joueur


    @staticmethod
    def personnages_non_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso non joueurs 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_joueur = %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : "-1"})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso_non_joueur = []
        for i in liste_entite: 
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                entite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                enti_obj = cursor.fetchone()
                liste_objet = []
                for i in enti_obj["id_objet"]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            liste_perso_non_joueur.append(Personnage(personnage["classe"], personnage["race"], personnage["lore"],entite["id_joueur"], i, entite["nom_entite"], caract, liste_objet))
        return liste_perso_non_joueur

    @staticmethod
    def monstres(id_campagne):# Cette fonction renvoie l'ensemble des monstres 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso_joueur = []
        for i in liste_entite: 
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                entite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Monstre "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                monstre = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                enti_obj = cursor.fetchone()
                liste_objet = []
                for i in enti_obj["id_objet"]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            liste_perso_joueur.append(Monstre(monstre["type"], entite["id_joueur"], entite["id_entite"], caract, liste_objet))
        return liste_perso_joueur

    @staticmethod
    def donjons():# Cette fonction renvoie l'ensemble des donjons
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_donjon "\
                    "FROM Donjon "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                liste_id_donjon = cursor.fetchall()
                liste_id_donjon = [liste_id_donjon[i]["id_donjon"] for i in range(0, len(liste_id_donjon))]
        liste_donjon = []
        for id_donjon in liste_id_donjon:
            liste_salle = []
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Donjon "\
                        "WHERE (id_donjon = %(id_donjon)s) "\
                        , {"id_donjon" : id_donjon})
                    donjon = cursor.fetchone()
                    donjon = [donjon["id_donjon"], donjon["nom_donjon"]]
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Salle "\
                        "WHERE (id_donjon = %(id_donjon)s) "\
                        , {"id_donjon" : id_donjon})
                    salle = cursor.fetchall()
                    salle = [[salle[i]["id_salle"] for i in range(0, len(salle))], [salle[i]["nom_salle"] for i in range(0, len(salle))], [salle[i]["coordonnee_salle_x"] for i in range(0, len(salle))] , [salle[i]["coordonnee_salle_y"] for i in range(0, len(salle))]]
            for id_salle in salle[0]: 
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT * "\
                            "FROM Salle_Objet "\
                            "WHERE (id_salle = %(id_salle)s) "\
                            , {"id_salle" : id_salle})
                        salle_objet = cursor.fetchall()
                        if salle_objet != None:
                            salle_objet = [salle_objet[i]["id_objet"] for i in range(0, len(salle_objet))]
                        else :
                            salle_objet = []
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT id_cellule "\
                            "FROM Cellule "\
                            "WHERE (id_salle = %(id_salle)s) "\
                            , {"id_salle" : id_salle})
                        cellule = cursor.fetchone()
                        cellule = cellule["id_cellule"]
                liste_objet = []
                for id_objet in salle_objet: 
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "SELECT * "\
                                "FROM Objet "\
                                "WHERE (id_objet = %(id_objet)s) "\
                                , {"id_objet" : id_objet})
                            objet = cursor.fetchone()
                            objet = [objet["id_objet"], objet["nom_objet"], objet["description_obj"]]
                    liste_objet.append(Objet(id_objet = objet[0], nom_objet = objet[1], description = objet[2]))
                liste_salle.append(Salle(id_salle = id_salle, nom_salle = salle[1][0], objets = liste_objet))
            liste_donjon.append(Donjon(id_donjon = id_donjon, nom_donjon = donjon[1][id_donjon], pieces = liste_salle))
        return liste_donjon

    @staticmethod
    def dict_entites(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite, nom_entite "\
                    "FROM Entite "\
                    "WHERE id_campagne=%(nom)s"\
                    ,{"nom" : id_campagne}
                )
                res = cursor.fetchall()        
        liste_entite = [dict(row) for row in res]
        return liste_entite

    @staticmethod
    def dict_monstres(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite, nom_entite "\
                    "FROM Monstre JOIN Entite ON Monstre.id_entite = Entite.id_entite "\
                    "WHERE id_campagne=%(nom)s"\
                    ,{"nom" : id_campagne}
                )
                res = cursor.fetchall()        
        liste_monstres = [dict(row) for row in res]
        return liste_monstres    

    @staticmethod
    def dict_personnages(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Personnage.id_entite, nom_entite "\
                    "FROM Personnage JOIN Entite ON Personnage.id_entite = Entite.id_entite "\
                    "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (username <> %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : Session.utilisateur.identifiant})
                res = cursor.fetchall()        
        liste_perso = [dict(row) for row in res]
        return liste_perso    
    
    @staticmethod
    def dict_pnj(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Personnage.id_entite, nom_entite "\
                    "FROM Personnage JOIN Entite ON Personnage.id_entite = Entite.id_entite "\
                    "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (username = %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : Session.utilisateur.identifiant})
                res = cursor.fetchall()        
        liste_pnj = [dict(row) for row in res]
        return liste_pnj
