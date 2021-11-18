from objets_metier.donjon import Salle
from utils.singleton import Singleton
from web.dao.cellule_dao import CelluleDAO
from web.dao.db_connection import DBConnection


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

    @staticmethod
    def ajoute_salle_rectangulaire(id_donjon: int, coordonnees_salle_donjon_x: int, coordonnees_salle_donjon_y: int, nom_salle: str):
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
            for x in range(1, coordonnees_salle_donjon_x+1):
                for y in range(1, coordonnees_salle_donjon_y+1):
                    CelluleDAO.add_cellule(id_salle, x, y)
            