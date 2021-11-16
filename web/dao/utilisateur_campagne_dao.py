from web.dao.campagne_dao import CampagneDAO
from web.dao.db_connection import DBConnection

class UtilisateurCampagneDao:

    @staticmethod
    def add_utilisateur_campagne(username : str, id_campagne : int, est_joueur : bool):
        if username not in CampagneDAO.trouve_joueurs():
            with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "INSERT INTO Utilisateur_Campagne (username, "\
                                                            "id_campagne, "\
                                                            "est_joueur) "\
                            "VALUES "\
                            "(%(username)s,%(id_campagne)s, %(est_joueur)%)"\
    
                        , {"username" : username
                        , "id_entite" : id_campagne
                        , "est_joueur" : est_joueur
                        })
            
