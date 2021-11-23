from datetime import date

from objets_metier.feedback import FeedBack
from web.dao.feed_back_dao import FeedBackDAO


class FeedBackService:
    """
    Cette classe fournit les services permettant de communiquer par feed-backs.
    """

    @staticmethod
    def donne_feedback(identifiant_joueur: int, message: str):
        FeedBackDAO.donner_feedback(identifiant_joueur, FeedBack(id_feedback = -1, message = message, date_ecriture = date.today()))

    @staticmethod
    def consulter_tous_les_feedbacks(): 
        return FeedBackDAO.consulter_tous()

    @staticmethod
    def consulter_tous_ses_feedbacks(identifiant_joueur): 
        return FeedBackDAO.consulter_tous_ses_feedbacks(identifiant_joueur) 
