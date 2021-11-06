from pydantic.main import ModelMetaclass
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton
import requests as req
from abc import abstractstaticmethod

from objets_metier.objet import Objet

class ObjetDAO(metaclass = Singleton):

    @staticmethod
    def add_objet(objet : Objet): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Objet (nom_objet, "\
                                            "description)"\
                        "VALUES "\
                        "(%(nom_objet)s, %(description)s)"\
   
                    , {"nom_objet" : objet.nom_objet
                    , "description" : objet.description
                    })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_objet) as max FROM Objet")
                    id_obj = cursor.fetchone()
                    id_obj = id_obj['max']
        return Objet(id_obj,objet.nom_objet, objet.description)
