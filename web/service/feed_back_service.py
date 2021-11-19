from objets_metier.feedback import FeedBack
from web.dao.feed_back_dao import FeedBackDAO


class FeedBackService:
    """
    Cette classe fournit les services permettant de communiquer par feed-backs.
    """

    @staticmethod
    def add_feedback(username : str, feed : FeedBack):
        FeedBackDAO.add_feedback(username, feed)

    @staticmethod
    def consulter_tous_les_feedbacks(): 
        return FeedBackDAO.consulter_tous()

    @staticmethod
    def creation_compte(identifiant, mot_de_passe, est_admin):         
        FeedBackDAO.createUtilisateur(identifiant, mot_de_passe, est_admin)

    @staticmethod
    def verifie_mdp(utilisateur_nom: str, mdp):
        return FeedBackDAO.verifie_mdp(utilisateur_nom, mdp)

    @staticmethod
    def utilisateur_admin(utilisateur_nom: str):
        return FeedBackDAO.getUtilisateurAdmin(utilisateur_nom)

    @staticmethod
    def est_utilisateur(nom: str):
        return FeedBackDAO.getUtilisateur(nom)

    def trouver_perso(id_campagne : int, id_joueur : int):
        return FeedBackDAO.trouver_perso(id_campagne, id_joueur)
