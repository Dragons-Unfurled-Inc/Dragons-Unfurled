from web.dao.db_connection import DBConnection


class AdministrateurDAO:

    @staticmethod
    def supprimer_compte(utilisateur_nom: str):
        #utilisateur_a_supprimer: Utilisateur = UtilisateurDAO.getUtilisateur(nom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Utilisateur "\
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
