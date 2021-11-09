from objets_metier.feedback import Feedback
from web.dao.feed_back_dao import FeedBackDAO

class FeedbackService() :

    @staticmethod
    def add_feedback(username : str, feed : Feedback):
        FeedBackDAO.add_feedback(username, feed)