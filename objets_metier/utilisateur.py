from abc import abstractmethod
from datetime import date
from typing import Any, List

from pydantic import BaseModel
from web.dao.feed_back_dao import FeedBackDAO

from objets_metier.feedback import FeedBack


class Utilisateur(BaseModel):

    identifiant : str
    
    def __init__(self,identifiant : str):
        super().__init__(
        identifiant = identifiant)
        
    class Config:
        schema_extra = {
            "example": {
                "identifiant": "essai_manon"
            }
        }
        
    def se_connecter(self, id : str, mdp : str):
        None
    
    def creer_compte(self, id : str, mdp : str):
        None
    
    def se_deconnecter(self):
        None 

    @staticmethod
    def ecrire_un_feed_back(message: str): 
        from client.vue.session import Session
        FeedBackDAO.donner_feedback(Session.utilisateur.identifiant, FeedBack(-1, message, date.today()))
    
    def consulter_ses_feed_back(): 
        FeedBackDAO.consulter_feed_back()
