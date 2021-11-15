from typing import List,Any
from pydantic import BaseModel
from objets_metier.feedback import Feedback

class Utilisateur(BaseModel):

    identifiant : str

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

    def donner_feed_back(self, message : str):
        None
    
    def consulter_feed_back(self):
        None
