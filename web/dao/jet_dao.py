from client.vue.session import Session
from web.dao.db_connection import DBConnection
from objets_metier.jet import Jet

class JetDAO:

    @staticmethod
    def add_jet(jet : Jet, username : str, choix_revel : bool) :
        id_camp = Session.id_campagne
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Jet (resultat, revelation, username, id_campagne)" \
                        "VALUES "\
                        "(%(resultat)s,%(revelation)s,%(username)s,%(id_campagne)s)"\
   
                    , {"resultat" : jet.valeur_jet
                    , "revelation" : choix_revel
                    , "username" : username
                    , "id_campagne": id_camp
                    })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_jet) as max FROM Jet")
                    id_jet = cursor.fetchone()
                    id_jet = id_jet['max']
        return id_jet


    @staticmethod
    def consulter_tous_les_jets(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Jet "\
                    "WHERE revelation = TRUE AND id_campagne = %(id_campagne)s;"\
                        , { "id_campagne": id_campagne})
                jet = cursor.fetchall()
        liste_print_jet = []
        for i in range(0, len(jet)):
            liste_print_jet.append(jet[i]["username"] + " a fait un jet d'une valeur de " + str(jet[i]["resultat"]))
        return liste_print_jet

    @staticmethod
    def consulter_tous_les_jets_mj(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Jet "\
                    "WHERE id_campagne = %(id_campagne)s;"\
                        , { "id_campagne": id_campagne})
                jet = cursor.fetchall()
        liste_print_jet = []
        for i in range(0, len(jet)):
            liste_print_jet.append(jet[i]["username"] + " a fait un jet d'une valeur de " + str(jet[i]["resultat"]))
        return liste_print_jet    
        

