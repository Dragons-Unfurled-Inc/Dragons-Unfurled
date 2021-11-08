from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.donjon import Salle

class SalleDAO(metaclass=Singleton): 

    @staticmethod
    def add_salle(id_donjon : int, coordonnees_salle_x : int, coordonnees_salle_y : int, salle :Salle):
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
                    , "coordonnee_salle_x" : coordonnees_salle_x
                    , "coordonnee_salle_y" : coordonnees_salle_y
                    , "id_donjon" : id_donjon
                    })