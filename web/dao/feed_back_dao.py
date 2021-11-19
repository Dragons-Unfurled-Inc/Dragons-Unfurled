from objets_metier.feedback import FeedBack
from web.dao.db_connection import DBConnection


class FeedBackDAO:

    @staticmethod
    def donner_feedback(username: str, feed: FeedBack): 
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

    @staticmethod
    def consulter_tous():
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Feedback ")
                feed_backs = cursor.fetchall()
        return feed_backs

    @staticmethod
    def consulter_tous_ses_feedbacks(identifiant):
        nom_utilisateur = identifiant
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Feedback "\
                    "WHERE username = %(username)s;"
                    , {"username" : nom_utilisateur})
                feed = cursor.fetchall()
        return feed
