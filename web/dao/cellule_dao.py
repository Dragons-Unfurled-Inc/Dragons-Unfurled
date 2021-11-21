from pydantic.main import ModelMetaclass
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection


class CelluleDAO(metaclass=Singleton):

    @staticmethod
    def add_cellule(id_salle : int, coord_x : int, coord_y : int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO Cellule (coordonnee_cellule_x, "\
                                            "coordonnee_cellule_y, "\
                                            "id_salle) "\
                    "VALUES "\
                    "(%(coordonnee_cellule_x)s,%(coordonnee_cellule_y)s,%(id_salle)s)"\

                , {"coordonnee_cellule_x" : coord_x
                , "coordonnee_cellule_y" : coord_y
                , "id_salle" : id_salle
                })        

    @staticmethod
    def trouve_id_cellule(id_salle: int, coordonnee_x: int, coordonnee_y: int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Cellule "\
                    "WHERE (coordonnee_cellule_x = %(coordonnee_cellule_x)s) "\
                    "AND (id_salle = %(id_salle)s) "\
                    "AND (coordonnee_cellule_y = %(coordonnee_cellule_y)s)"\
                    , {"coordonnee_cellule_x": coordonnee_x, "id_salle": id_salle, "coordonnee_cellule_y": coordonnee_y})
                res = cursor.fetchone()
        if res == None:
            id_cellule = None
        else:
            id_cellule = dict(res)["id_cellule"]
        return id_cellule

    @staticmethod
    def coordonnees_cellules_salle(id_salle):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Cellule FULL OUTER JOIN Salle ON Cellule.id_salle = Salle.id_salle "\
                    "WHERE (Salle.id_salle = %(id_salle)s) ;"\
                    , {"id_salle": id_salle})
                res = cursor.fetchall()
        if res == None:
            coordonnees_cellules_salle = []
        else:
            coordonnees_cellules_salle = []
            for ligne in res:
                coordonnees_cellules_salle.append([dict(ligne)["coordonnee_cellule_x"], dict(ligne)["coordonnee_cellule_y"]])
        return coordonnees_cellules_salle
