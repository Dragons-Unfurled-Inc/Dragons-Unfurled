from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.objet import Objet
from objets_metier.salle import Salle
from web.dao.objet_dao import ObjetDAO

class ObjetSalleDAO(metaclass = Singleton):

    @staticmethod
    def add_salle_objet(salle : Salle):
        if salle.objets != None:
            for i in range(0, len(salle.objets)):
                obj = Objet(salle.objets[i]["id_objet"], salle.objets[i]["nom_objet"], salle.objets[i]["description"])
                objet = ObjetDAO.add_objet(obj)
                with DBConnection().connection as connection:
                        with connection.cursor() as cursor :
                            cursor.execute(
                                "INSERT INTO Salle_objet (id_salle, "\
                                                        "id_objet)"\
                                "VALUES "\
                                "(%(id_salle)s, %(id_objet)s)"\
        
                            , { "id_salle" : salle.id_salle
                            , "id_objet" : objet.id_objet
                            })