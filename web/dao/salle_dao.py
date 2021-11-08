from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.donjon import Salle

class SalleDAO(metaclass=Singleton): 

    @staticmethod
    def add_salle(id_donjon : int, salle :Salle):
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