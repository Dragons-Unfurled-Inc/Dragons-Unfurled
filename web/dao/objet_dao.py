from objets_metier.objet import Objet
from utils.singleton import Singleton
from web.dao.cellule_dao import CelluleDAO
from web.dao.db_connection import DBConnection
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO


class ObjetDAO(metaclass = Singleton): 

    @staticmethod
    def trouve_id_obj(x,y, id_salle) :
        id_cellule = CelluleDAO.trouve_id_cellule(id_salle, x, y)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Objet "\
                    "WHERE (id_cellule = %(id_cellule)s) "\
                    , {"id_cellule": id_cellule})
                res = cursor.fetchone()
        if res == None:
            id_objet = None
        else:
            id_objet = dict(res)["id_objet"]
        return id_objet

    @staticmethod
    def trouve_id_ent(x,y, id_salle) :
        id_cellule = CelluleDAO.trouve_id_cellule(id_salle, x, y)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite "\
                    "WHERE (id_cellule = %(id_cellule)s) "\
                    , {"id_cellule": id_cellule})
                res = cursor.fetchone()
        if res == None:
            id_objet = None
        else:
            id_objet = dict(res)["id_entite"]
        return id_objet

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
                    , "id_objet" : int(id_objet)
                    })
        MaitreDuJeuDAO.retirer_objet_salle(id_objet)
        
