from objets_metier.feedback import Feedback
from web.dao.db_connection import DBConnection
from objets_metier.utilisateur import Utilisateur

class FeedBackDAO:

    @staticmethod
    def add_feedback(feed : Feedback, username : str): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Feedback (message, "\
                                               "date_ecriture, "\
                                               "username ) "\

                        "VALUES "\
                        "(%(message)s,%(date_ecriture)s,%(username)s);", 
                        { "message" : feed.message
                        , "date_ecriture": feed.date_ecriture
                        , "username" : username}
                    )
        return feed

    @staticmethod
    def consulter_tous():
        return []

    @staticmethod
    def consulter_ses_feed_backs(utilisateur: Utilisateur):
        return []