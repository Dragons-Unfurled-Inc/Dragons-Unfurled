
from pydantic import BaseModel

from objets_metier.feedback import FeedBack


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

    @staticmethod
    def ecrire_un_feed_back(message: str): 
        from client.vue.session import Session
        from client.web_client.feed_back_client import FeedBackClient
        FeedBackClient.donne_feedback(Session.utilisateur.identifiant, message) 
    
    def consulter_ses_feed_back(): 
        from client.web_client.feed_back_client import FeedBackClient
        feed_backs = FeedBackClient.consulter_feed_back()
        for ligne in feed_backs:
            info = dict(ligne)
            print(info["username"],"\n",FeedBack(id_feedback = info["id_feedback"], message = info["message"], date_ecriture = info["date_ecriture"]), "\n\n")
<<<<<<< HEAD
=======

    def str(self):
        """
        permet un affichage des caractéristiques
        """
        modele = '\n'.join(
                       'Identifiant : {}')
        return modele.format(
            self.identifiant)
        
>>>>>>> 2dfa5638b141c39a21e31f58517e5e0a6079073a
