from pydantic.main import ModelMetaclass
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton 


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
                    , "coordonnee_cellule_y" :coord_y
                    , "id_salle" : id_salle
                    })        