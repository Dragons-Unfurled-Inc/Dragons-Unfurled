from web.dao.joueur_dao import JoueurDAO


class JoueurService() :

    @staticmethod
    def noms_utilisateurs():
        return JoueurDAO.liste_noms()
            