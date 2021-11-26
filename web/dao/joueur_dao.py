from web.dao.db_connection import DBConnection

class JoueurDAO:

    @staticmethod
    def liste_noms():
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT username "\
                    "FROM utilisateur "\
                    "WHERE est_administrateur = False"
                )
                res = cursor.fetchall()
        liste_nom = [dict(row)["username"] for row in res] # Nous récupérons la liste des noms à partir de res. res peut être par exemple de la forme : [RealDictRow([('username', 'Isabelle')]), RealDictRow([('username', 'Thomas')])]
        return liste_nom