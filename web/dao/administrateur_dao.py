from web.dao.db_connection import DBConnection


class AdministrateurDAO:

    @staticmethod
    def supprimer_compte(utilisateur_nom: str): # Nous supprimons toutes les informations liées à Thomas avant d'effacer son compte.
        AdministrateurDAO.supprimer_entites_utilisateur(utilisateur_nom) # Nous aurions pu, à la place, retirer son nom en tant que clef secondaire, c'est un choix.
        AdministrateurDAO.supprimer_feed_backs_utilisateur(utilisateur_nom)
        AdministrateurDAO.supprimer_jets_utilisateur(utilisateur_nom)
        AdministrateurDAO.supprimer_campagne_utilisateur(utilisateur_nom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Utilisateur "\
                    "WHERE username = %(nom)s;"\
                    , {"nom": utilisateur_nom})
                    
    @staticmethod
    def supprimer_entites_utilisateur(utilisateur_nom):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Utilisateur_Entite "\
                    "WHERE username = %(nom)s;"\
                    , {"nom": utilisateur_nom})

    @staticmethod
    def supprimer_feed_backs_utilisateur(utilisateur_nom):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM FeedBack "\
                    "WHERE username = %(nom)s;"\
                    , {"nom": utilisateur_nom})

    @staticmethod
    def supprimer_jets_utilisateur(utilisateur_nom):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Jet "\
                    "WHERE username = %(nom)s;"\
                    , {"nom": utilisateur_nom})

    @staticmethod
    def supprimer_campagne_utilisateur(utilisateur_nom):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Utilisateur_Campagne "\
                    "WHERE username = %(nom)s;"\
                    , {"nom": utilisateur_nom})

    @staticmethod
    def ajouter_droits_administrateur(utilisateur_nom: str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Utilisateur "\
                    "SET est_administrateur = %(est_administrateur)s "\
                    "WHERE username = %(nom)s;"\
                    , {"est_administrateur" : True
                    , "nom": utilisateur_nom})

    @staticmethod
    def supprimer_droits_administrateur(utilisateur_nom: str):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Utilisateur "\
                    "SET est_administrateur = %(est_administrateur)s "\
                    "WHERE username = %(nom)s;"\
                    , {"est_administrateur" : False
                    , "nom": utilisateur_nom})
