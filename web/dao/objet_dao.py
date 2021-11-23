from objets_metier.objet import Objet
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection


class ObjetDAO(metaclass = Singleton): 

    @staticmethod
    def ajouter_objet(objet : Objet): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Objet (nom_objet, "\
                                            "description_obj)"\
                        "VALUES "\
                        "(%(nom_objet)s, %(description_obj)s)"\
   
                    , {"nom_objet" : objet.nom_objet
                    , "description" : objet.description_obj
                    })

    @staticmethod
    def ajouter_objet_et_recuperation(objet : Objet): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Objet (nom_objet, "\
                                            "description_obj)"\
                        "VALUES "\
                        "(%(nom_objet)s, %(description_obj)s)"\
   
                    , {"nom_objet" : objet.nom_objet
                    , "description" : objet.description_obj
                    })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_objet) as max FROM Objet")
                    id_obj = cursor.fetchone()
                    id_obj = id_obj['max']
        return Objet(id_obj,objet.nom_objet, objet.description_obj)
