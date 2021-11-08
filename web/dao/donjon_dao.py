from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.donjon import Donjon

class DonjonDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_donjon(id_campagne : int, donjon : Donjon) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Donjon (nom_donjon, "\
                                            "id_campagne) "\
                        "VALUES "\
                        "(%(nom_donjon)s,%(id_campagne)s)"\
   
                    , {"nom_donjon" : donjon.nom_donjon
                    , "id_campagne" : id_campagne
                    })