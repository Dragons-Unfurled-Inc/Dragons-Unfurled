from objets_metier.feedback import Feedback
from web.dao.db_connection import DBConnection
from objets_metier.utilisateur import Utilisateur

class FeedBackDAO:

    @staticmethod
    def add_feedback(username : str, feed : Feedback): 
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
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Feedback ")
                feed = cursor.fetchall()
        for ligne in feed:
            info = dict(ligne)
            print(Feedback(info["id_feedback"], info["message"], info["date_ecriture"]) + "\n\n" )

    @staticmethod
    def consulter_ses_feed_backs(utilisateur: Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Feedback "\
                    "WHERE username = %(username)s;"
                    , {"username" : utilisateur.identifiant})
                feed = cursor.fetchone()
        for i in range(len(feed["id_feedback"])):
            print(Feedback(feed["id_feedback"][i], feed["message"][i], feed["date_ecriture"][i]) + "\n\n" )