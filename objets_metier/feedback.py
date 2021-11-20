import datetime
from pydantic import BaseModel
class FeedBack(BaseModel):

    id_feedback: int
    message: str
    date_ecriture: datetime.date
    
    class Config:
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
        modele ='\n'.join(['Identifiant : {} \nLe message est : {} \nDate du message : {}'])
        return modele.format(self.id_feedback,
                             self.message,
                             self.date_ecriture)
