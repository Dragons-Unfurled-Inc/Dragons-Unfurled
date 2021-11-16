from abc import abstractmethod
from typing import List,Any
from pydantic import BaseModel
from objets_metier.feedback import FeedBack 
from web.dao.feed_back_dao import FeedBackDAO
from datetime import date

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
    def ecrire_son_feed_back(message: str): # Cette fonction va écraser l'ancien feed-back, et en entrer un nouveau, c'est un choix que nous avons fait pour éviter les spams. 
        from client.vue.session import Session
        print(FeedBack(-1, message, date.today()))
        print(date.today())
        FeedBackDAO.donner_feedback(Session.utilisateur.identifiant, FeedBack(-1, message, date.today()))
    
    def consulter_son_feed_back(): # Cela permet de récupérer ce qu'on avait écrit pour pouvoir faire un copier collé, de se relire, mais surtout de regardé si nous avons reçu une réponse de la part d'un administrateur.
        FeedBackDAO.consulter_feed_back()
