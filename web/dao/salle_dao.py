import random
from typing import List

from objets_metier.donjon import Salle
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
