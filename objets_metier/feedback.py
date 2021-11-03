import datetime
from pydantic import BaseModel
class Feedback(BaseModel):

    _id_feedback: str
    _message: str
    _date_ecriture: datetime.date
    
    class Config:
        underscore_attrs_are_private = True


    def __str__(self):
        """
        Affichage des feedbacks
        """
        modele = '\n'.join(['Identifiant : {} \nLe message est : {} \nDate du message : {}'])
        return modele.format(self._id_feedback,
                             self._message,
                             self._date_ecriture)

    @property
    def id_feedback(self):
        return self._id_feedback

    @id_feedback.setter
    def id_feedback(self, value):
        self._id_feedback = value   

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def date_ecriture(self):
        return self._date_ecriture

    @date_ecriture.setter
    def date_ecriture(self, value):
        self._date_ecriture = value        