from web.dao.db_connection import DBConnection
from objets_metier.jet import Jet
from objets_metier.utilisateur import Utilisateur

class JetDAO:

    @staticmethod
    def add_jet(jet : Jet, username : str, choix_revel : bool) :
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Jet (resultat, "\
                                         "revelation, "\
                                         "username)"\
                        "VALUES "\
                        "(%(resultat)s,%(revelation)s,%(username)s)"\
   
                    , {"resultat" : jet.valeur_jet
                    , "revelation" : choix_revel
                    , "username" : username
                    })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_jet) as max FROM Jet")
                    id_jet = cursor.fetchone()
                    id_jet = id_jet['max']
        return id_jet


    @staticmethod
    def consulter_tous_les_jets():
        return []

