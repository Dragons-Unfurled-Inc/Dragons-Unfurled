from web.dao.db_connection import DBConnection

class UtilisateurCampagneDao:

    @staticmethod
    def add_utilisateur_campagne(username : str, id_entite : int):
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Utilisateur_entite (username, "\
                                                        "id_entite) "\
                        "VALUES "\
                        "(%(username)s,%(id_entite)s)"\
   
                    , {"username" : username
                    , "id_entite" : id_entite
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
    