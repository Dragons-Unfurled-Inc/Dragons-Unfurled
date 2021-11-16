import datetime
from pydantic import BaseModel
class FeedBack(BaseModel):

    id_feedback: int
    message: str
    date_ecriture: datetime.date
    
    class Config:
        underscore_attrs_are_private = True
        schema_extra = {
            "example": {
                "id_feedback" : 4,
                "message" : "jessaye la bdd",
                "date_ecriture" : datetime.date.today    
            }
        }


    def __str__(self):
        """
        Affichage des feedbacks
        """
        modele = '\n'.join(['Identifiant : {} \nLe message est : {} \nDate du message : {}'])
        return modele.format(self.__id_feedback,
                             self.__message,
                             self.__date_ecriture)

    @property
    def id_feedback(self):
        return self.__id_feedback

    @id_feedback.setter
    def id_feedback(self, value):
        self.__id_feedback = value   

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def date_ecriture(self):
        return self.__date_ecriture

    @date_ecriture.setter
    def date_ecriture(self, value):
        self.__date_ecriture = value        