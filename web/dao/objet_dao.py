from objets_metier.objet import Objet
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO


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
                    , "description_obj" : objet.description_obj
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
                    , "description_obj" : objet.description_obj
                    })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_objet) as max FROM Objet")
                    id_obj = cursor.fetchone()
                    id_obj = id_obj['max']
        return Objet(id_objet = id_obj,nom_objet = objet.nom_objet, description_obj = objet.description_obj)

    @staticmethod
    def ramasse_entite_objet(id_entite, id_objet):
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Entite_Objet (id_entite, "\
                                            "id_objet)"\
                        "VALUES "\
                        "(%(id_entite)s, %(id_objet)s)"\
   
                    , {"id_entite" : id_entite
                    , "id_objet" : id_objet
                    })
        MaitreDuJeuDAO.retirer_objet_salle(id_objet)
        
