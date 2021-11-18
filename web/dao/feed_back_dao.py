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
                feed = cursor.fetchall()
        for ligne in feed:
            info = dict(ligne)
            print(info["username"],"\n", FeedBack(id_feedback = info["id_feedback"], message = info["message"], date_ecriture = info["date_ecriture"]), "\n\n")

    @staticmethod
    def consulter_feed_back():
        from client.vue.session import Session
        nom_utilisateur = Session.utilisateur.identifiant
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Feedback "\
                    "WHERE username = %(username)s;"
                    , {"username" : nom_utilisateur})
                feed = cursor.fetchall()
        for ligne in feed:
            info = dict(ligne)
            print(FeedBack(id_feedback = info["id_feedback"], message = info["message"], date_ecriture = info["date_ecriture"]), "\n\n")
