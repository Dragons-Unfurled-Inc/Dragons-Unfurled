from pydantic.main import ModelMetaclass
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton 


class CelluleDAO(metaclass=Singleton):

    @staticmethod
    def add_cellule(coord_x : int, coord_y : int):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Cellule (nom_donjon, "\
                                              "id_campagne) "\
                        "VALUES "\
                        "(%(nom_donjon)s,%(id_campagne)s)"\
   
                    , {
                    })        