from client.vue.session import Session
from objets_metier.entite import Entite
from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection


class UtilisateurEntiteDao:

    @staticmethod
    def ajoute_utilisateur_entite(entite : Entite):
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Utilisateur_entite (username, "\
                                                        "id_entite) "\
                        "VALUES "\
                        "(%(username)s,%(id_entite)s)"\
   
                    , {"username" : Session.utilisateur.identifiant
                    , "id_entite" : entite.id_entite
                    })
                    
    @staticmethod
    def importe_utilisateur_entite(dic):
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Utilisateur_entite (username, "\
                                                        "id_entite) "\
                        "VALUES "\
                        "(%(username)s,%(id_entite)s)"\
   
                    , {"username" : dic['username']
                    , "id_entite" : dic['id_entite']
                    })
                    
    def trouve_enti(username): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_entite as entis FROM Utilisateur_Entite WHERE username = %(username)s ; "
                    ,{"username" : username})
                    entis = cursor.fetchall()
                    res = []
                    for dic in entis :
                        res.append(dic['entis'])
                return res
    