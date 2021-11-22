from client.vue.session import Session
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection
from web.dao.salle_dao import SalleDAO


class DonjonDAO(metaclass=Singleton):
    
    @staticmethod    
    def ajoute_donjon(nom_donjon: str, taille_salle_donjon_x, taille_salle_donjon_y):
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO Donjon (nom_donjon, "\
                                        "id_campagne) "\
                    "VALUES "\
                    "(%(nom_donjon)s,%(id_campagne)s)"\

                , {"nom_donjon" : nom_donjon
                , "id_campagne" : id_campagne
                })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_donjon) as max FROM Donjon")
                    res = cursor.fetchone()
                    id_donjon = res['max']
        SalleDAO.ajoute_salle_rectangulaire(id_donjon, taille_salle_donjon_x, taille_salle_donjon_y, "Salle principale", 0, 0)
            
    @staticmethod
    def dict_donjons():# Cette fonction renvoie un dictionnaire des donjons.
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_donjon, nom_donjon "\
                    "FROM Donjon "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                res = cursor.fetchall()
                if res != None:
                    liste_dict_donjons = [dict(row) for row in res] 
                else:
                    liste_dict_donjons = []
        return liste_dict_donjons

    @staticmethod
    def existe_donjon_campagne(id_donjon):
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_donjon "\
                    "FROM Donjon "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_donjon = %(id_donjon)s)"\
                    , {"id_campagne" : id_campagne, "id_donjon" : id_donjon})
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    @staticmethod
    def existe_salle_donjon(id_salle):
        from client.vue.session import Session
        id_donjon = Session.id_donjon
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_salle "\
                    "FROM Salle "\
                    "WHERE (id_donjon = %(id_donjon)s) "\
                    "AND (id_salle = %(id_salle)s)"\
                    , {"id_donjon" : id_donjon, "id_salle" : id_salle})
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    @staticmethod
    def espace_libre_salle(x, y):
        from client.vue.session import Session
        id_donjon = Session.id_donjon
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Salle "\
                    "WHERE (id_donjon = %(id_donjon)s) "\
                    "AND (coordonnee_salle_x = %(coordonnee_salle_x)s) "\
                    "AND (coordonnee_salle_y = %(coordonnee_salle_y)s)"\
                    , {"id_donjon" : id_donjon, "coordonnee_salle_x" : x, "coordonnee_salle_y" : y})
                res = cursor.fetchone()
        if res != None:
            return False
        else : 
            return True
