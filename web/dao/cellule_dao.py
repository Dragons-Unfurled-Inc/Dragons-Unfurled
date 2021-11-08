from pydantic.main import ModelMetaclass
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton 


class CelluleDAO(metaclass=Singleton):

    @staticmethod
    def add_cellule(id_salle : int, coord_x : int, coord_y : int):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Cellule (coordonnees_cellule_x, "\
                                              "coordonnees_celulle_y, "\
                                              "id_salle) "\
                        "VALUES "\
                        "(%(coordonnees_cellule_x)s,%(coordonnees_celulle_y)s,%(id_salle)s)"\
   
                    , {"coordonnees_cellule_x" : coord_x
                    , "coordonnees_cellule_y" :coord_y
                    , "id_salle" : id_salle
                    })        