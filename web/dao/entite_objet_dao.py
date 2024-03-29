from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.entite import Entite
from web.dao.objet_dao import ObjetDAO

class ObjetEntiteDAO(metaclass = Singleton):

    @staticmethod
    def add_entite_objet(enti : Entite):
        for i in range(0, len(enti.objets)):
            objet = ObjetDAO.add_objet(enti.objets[i])
            with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "INSERT INTO Entite_objet (id_entite, "\
                                                    "id_objet)"\
                            "VALUES "\
                            "(%(id_entite)s, %(id_objet)s)"\
    
                        , { "id_entite" : enti.id_entite
                        , "id_objet" : objet.id_objet
                        })
                        
    def import_entite_objet(dic):
        with DBConnection().connection as connection:
                 with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Entite_objet (id_entite, "\
                                                    "id_objet)"\
                        "VALUES "\
                        "(%(id_entite)s, %(id_objet)s)"\
    
                        , { "id_entite" : dic['id_entite']
                        , "id_objet" : dic['id_objet']
                        })