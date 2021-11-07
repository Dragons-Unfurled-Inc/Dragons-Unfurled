from objets_metier.feedback import Feedback
from web.dao.feed_back_dao import FeedBackDAO

class FeedbackService() :

    @staticmethod
    def add_feedback(feed : Feedback, username : str):
        FeedBackDAO.add_feedback(feed, username)