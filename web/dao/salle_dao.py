import random
from typing import List

from objets_metier.objet import Objet
from objets_metier.salle import Salle
from objets_metier.personnage import Personnage
from objets_metier.monstre import Monstre
from objets_metier.caracteristique import Caracteristique
from utils.singleton import Singleton
from web.dao.cellule_dao import CelluleDAO
from web.dao.db_connection import DBConnection


class SalleDAO(metaclass=Singleton): 

    @staticmethod
    def add_salle(id_donjon : int, salle : Salle):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Salle (nom_salle, "\
                                            "coordonnee_salle_x, "\
                                            "coordonnee_salle_y,"\
                                            "id_donjon) "\
                        "VALUES "\
                        "(%(nom_salle)s,%(coordonnee_salle_x)s,%(coordonnee_salle_y)s,%(id_donjon)s)"\
   
                    , {"nom_salle" : salle.nom_salle
                    , "coordonnee_salle_x" : salle.coordonnees_salle_donjon[0]
                    , "coordonnee_salle_y" : salle.coordonnees_salle_donjon[1]
                    , "id_donjon" : id_donjon
                    })
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_salle) as max FROM Salle")
                    id_salle = cursor.fetchone()
                    id_salle = id_salle['max']
            return Salle(id_salle, salle.nom_salle, salle.coordonnees_salle_donjon, salle.coordonnees_salle_cellule, salle.objets, salle.entites)

    @staticmethod
    def ajoute_salle_rectangulaire(id_donjon: int, taille_salle_donjon_x: int, taille_salle_donjon_y: int, nom_salle: str, coordonnees_salle_donjon_x: int, coordonnees_salle_donjon_y: int):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Salle (nom_salle, "\
                                            "coordonnee_salle_x, "\
                                            "coordonnee_salle_y,"\
                                            "id_donjon) "\
                        "VALUES "\
                        "(%(nom_salle)s,%(coordonnee_salle_x)s,%(coordonnee_salle_y)s,%(id_donjon)s)"\
   
                    , {"nom_salle" : nom_salle
                    , "coordonnee_salle_x" : coordonnees_salle_donjon_x
                    , "coordonnee_salle_y" : coordonnees_salle_donjon_y
                    , "id_donjon" : id_donjon
                    })
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_salle) as max FROM Salle")
                    res = cursor.fetchone()
                    id_salle = res['max']
            for x in range(1, taille_salle_donjon_x+1):
                for y in range(1, taille_salle_donjon_y+1):
                    CelluleDAO.add_cellule(id_salle, x, y)
            
    @staticmethod
    def ajouter_salle_construite(id_donjon: int, coordonnees_salle_donjon_x: int, coordonnees_salle_donjon_y: int, nom_salle: str, coord_cellules: List[List[int]]):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Salle (nom_salle, "\
                                            "coordonnee_salle_x, "\
                                            "coordonnee_salle_y,"\
                                            "id_donjon) "\
                        "VALUES "\
                        "(%(nom_salle)s,%(coordonnee_salle_x)s,%(coordonnee_salle_y)s,%(id_donjon)s)"\
   
                    , {"nom_salle" : nom_salle
                    , "coordonnee_salle_x" : coordonnees_salle_donjon_x
                    , "coordonnee_salle_y" : coordonnees_salle_donjon_y
                    , "id_donjon" : id_donjon
                    })
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_salle) as max FROM Salle")
                    res = cursor.fetchone()
                    id_salle = res['max']
            for cellule in coord_cellules:
                CelluleDAO.add_cellule(id_salle, cellule[0], cellule[1]) # Notre code permet notamment d'avoir deux cellules au même endroit. 
                                                                         # Ça permet d'utiliser certaine variante de jeux de rôle pour avoir des monstre au même endroit, mais pas sur la même case. 
                                                                         # Par exemple, quand il y a des pieges, des espaces caché ou un underworld/ d'autres dimensions.

    @staticmethod
    def ajouter_entite_salle(identifiant_entite, identifiant_salle):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Cellule "\
                    "WHERE id_salle=%(id_salle)s"\
                    ,{"id_salle" : identifiant_salle})
                res = cursor.fetchall()
        liste_id_cellules = [dict(row)["id_cellule"] for row in res]
        nb_cellules = len(liste_id_cellules)
        if nb_cellules == 0:
            print("Il n'y a pas de cellules dans cette salle.")
        else:
            position_aleatoire = random.randint(0, nb_cellules-1)
            SalleDAO.ajouter_entite_cellule(identifiant_entite, liste_id_cellules[position_aleatoire])

    @staticmethod
    def ajouter_objet_salle(identifiant_salle, id_objet):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Cellule "\
                    "WHERE id_salle=%(id_salle)s"\
                    ,{"id_salle" : identifiant_salle})
                res = cursor.fetchall()
        liste_id_cellules = [dict(row)["id_cellule"] for row in res]
        nb_cellules = len(liste_id_cellules)
        if nb_cellules == 0:
            print("Il n'y a pas de cellules dans cette salle.")
        else:
            position_aleatoire = random.randint(0, nb_cellules-1)
            SalleDAO.ajouter_objet_cellule(id_objet, liste_id_cellules[position_aleatoire])

    @staticmethod
    def ajouter_entite_cellule(id_entite, id_cellule):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Entite "\
                    "SET id_cellule = %(id_cellule)s "\
                    "WHERE id_entite = %(id_entite)s;"\
                    , { "id_cellule": id_cellule
                    , "id_entite": id_entite})

    @staticmethod
    def ajouter_objet_cellule(id_objet, id_cellule):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Objet "\
                    "SET id_cellule = %(id_cellule)s "\
                    "WHERE id_objet = %(id_objet)s;"\
                    , { "id_cellule": id_cellule
                    , "id_objet": id_objet})

    @staticmethod
    def id_salle_contenant_entite(id_entite):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Salle FULL OUTER JOIN Cellule ON Salle.id_salle = Cellule.id_salle "\
                    "JOIN Entite ON Cellule.id_cellule = Entite.id_cellule "\
                    "WHERE (Entite.id_entite = %(id_entite)s) ;"\
                    , {"id_entite": id_entite})
                res = cursor.fetchone()
        if res == None:
            id_salle = None
        else:
            id_salle = dict(res)["id_salle"]
        return id_salle

    @staticmethod
    def id_salle_contenant_objet(id_objet):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Salle FULL OUTER JOIN Cellule ON Salle.id_salle = Cellule.id_salle "\
                    "JOIN Objet ON Cellule.id_cellule = Objet.id_cellule "\
                    "WHERE (Objet.id_objet = %(id_objet)s) ;"\
                    , {"id_objet": id_objet})
                res = cursor.fetchone()
        if res == None:
            id_salle = None
        else:
            id_salle = dict(res)["id_salle"]
        return id_salle
    
    @staticmethod
    def trouve_salle(id_salle):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Salle "\
                    "WHERE (id_salle = %(id_salle)s) "\
                    , {"id_salle" : id_salle})
                salle = cursor.fetchone()
                salle = [[salle["id_salle"]], [salle["nom_salle"]], [salle["coordonnee_salle_x"]], [salle["coordonnee_salle_y"]]]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Cellule "\
                    "WHERE (id_salle = %(id_salle)s) "\
                    , {"id_salle" : id_salle})
                cellule = cursor.fetchall()
                if cellule == None:
                    id_cellule = []
                else :
                    id_cellule = [cellule[i]["id_cellule"] for i in range(0, len(cellule))]
        liste_obj = []
        liste_enti = []
        for id_cell in id_cellule:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Objet "\
                        "WHERE (id_cellule = %(id_cellule)s) "\
                        , {"id_cellule" : id_cell})
                    objet = cursor.fetchall()
                    if objet == None :
                        id_objet = []
                    else:
                        id_objet = [objet[i]["id_objet"] for i in range(0, len(objet))]
            for i in range(0, len(id_objet)):
                liste_obj.append(Objet(id_objet = i, nom_objet = objet[i]["nom_objet"], description_obj = objet[i]["description_obj"]))
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_entite "\
                        "FROM Entite "\
                        "WHERE (id_cellule = %(id_cellule)s) "\
                        , {"id_cellule" : id_cell})
                    id_enti = cursor.fetchall()
                    if id_enti == None :
                        id_entite = []
                    else:
                        id_entite = [id_enti[i]["id_objet"] for i in range(0, len(id_enti))]
            for id_ent in id_entite : 
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT * "\
                            "FROM Personnage "\
                            "WHERE (id_entite = %(id_entite)s) "\
                            , {"id_entite" : id_ent})
                        perso = cursor.fetchone()
                        if perso != None :
                            with DBConnection().connection as connection:
                                with connection.cursor() as cursor:
                                    cursor.execute(
                                        "SELECT * "\
                                        "FROM Entite "\
                                        "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite"\
                                        "WHERE (id_entite = %(id_entite)s) "\
                                        , {"id_entite" : id_ent})
                                    enti_perso = cursor.fetchone()
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
                            with DBConnection().connection as connection:
                                with connection.cursor() as cursor:
                                    cursor.execute(
                                        "SELECT * "\
                                        "FROM Entite_Objet "\
                                        "JOIN Objet ON Entite_Objet.id_objet = Objet.id_objet"\
                                        "WHERE (id_entite = %(id_entite)s) "\
                                        , {"id_entite" : id_ent})
                                    objet_perso = cursor.fetchall()
                                    if objet_perso == None :
                                        id_objet_perso = []
                                    else:
                                        id_objet_perso = [objet_perso[i]["id_objet"] for i in range(0, len(objet_perso))]
                            liste_objet_perso = [] 
                            for i in range(len(id_objet_perso)):
                                liste_objet_perso.append(Objet(id_objet = objet_perso[i]["id_objet"], nom_objet = objet_perso[i]["nom_objet"], description_obj = objet_perso[i]["description_obj"]))
                            caract = Caracteristique(nom_entite = enti_perso["nom_entite"], force = enti_perso["force"], experience = enti_perso["experience"], intelligence = enti_perso["intelligence"], charisme = enti_perso["charisme"], dexterite = enti_perso["dexterite"], constitution = enti_perso["constitution"], vie = enti_perso["vie"], sagesse =  enti_perso["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = enti_perso["description"], classe_armure = enti_perso["classe_armure"])
                            perso = Personnage(classe = perso["classe"], race = perso["race"], lore = perso["lore"], id_joueur = enti_perso["username"], id_entite = enti_perso["id_entite"], nom_entite = enti_perso["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet_perso)
                            liste_enti.append(perso)
                        else : 
                            with DBConnection().connection as connection:
                                with connection.cursor() as cursor:
                                    cursor.execute(
                                    "SELECT * "\
                                    "FROM Monstre "\
                                    "WHERE (id_entite = %(id_entite)s) "\
                                    , {"id_entite" : id_ent})
                                    perso = cursor.fetchone()
                            with DBConnection().connection as connection:
                                with connection.cursor() as cursor:
                                    cursor.execute(
                                        "SELECT * "\
                                        "FROM Entite "\
                                        "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite"\
                                        "WHERE (id_entite = %(id_entite)s) "\
                                        , {"id_entite" : id_ent})
                                    enti_monstre = cursor.fetchone()
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
                            with DBConnection().connection as connection:
                                with connection.cursor() as cursor:
                                    cursor.execute(
                                        "SELECT * "\
                                        "FROM Entite_Objet "\
                                        "JOIN Objet ON Entite_Objet.id_objet = Objet.id_objet"\
                                        "WHERE (id_entite = %(id_entite)s) "\
                                        , {"id_entite" : id_ent})
                                    objet_monstre = cursor.fetchall()
                                    if objet_monstre == None :
                                        id_objet_monstre = []
                                    else:
                                        id_objet_monstre = [objet_monstre[i]["id_objet"] for i in range(0, len(objet_monstre))]
                            liste_objet_monstre = [] 
                            for i in range(len(id_objet_monstre)):
                                liste_objet_monstre.append(Objet(id_objet = objet_monstre[i]["id_objet"], nom_objet = objet_monstre[i]["nom_objet"], description_obj = objet_monstre[i]["description_obj"]))
                            caract = Caracteristique(nom_entite = enti_monstre["nom_entite"], force = enti_monstre["force"], experience = enti_monstre["experience"], intelligence = enti_monstre["intelligence"], charisme = enti_monstre["charisme"], dexterite = enti_monstre["dexterite"], constitution = enti_monstre["constitution"], vie = enti_monstre["vie"], sagesse =  enti_monstre["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = enti_monstre["description"], classe_armure = enti_monstre["classe_armure"])
                            monstre = Monstre(type = monstre["type"], id_joueur = enti_monstre["username"], id_entite = enti_monstre["id_entite"], nom_entite = enti_monstre["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet_monstre)
                            liste_enti.append(monstre)
            salle_retournee = Salle(id_salle = id_salle, nom_salle = salle[1][0], coordonnees_salle_donjon = [salle[2][0], salle[3][0]], coordonnees_salle_cellule = [[0,0], [1,1]], objets = liste_obj, entites = liste_enti )
            return salle_retournee