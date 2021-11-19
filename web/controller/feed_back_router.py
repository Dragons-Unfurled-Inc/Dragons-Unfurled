from fastapi import APIRouter
from objets_metier.utilisateur import Utilisateur
from web.service.feed_back_service import FeedBackService

routerf = APIRouter()
 

@routerf.get("/feed_backs/", tags=["feed_back"])
def obtenir_tous_les_feed_backs():
    return FeedBackService.consulter_tous_les_feedbacks()

@routerf.post("/identifiant_joueur/{identifiant_joueur}/message/{message}", tags=["feed_back"])
def donne_feedback(identifiant_joueur, message):
    FeedBackService.donne_feedback(identifiant_joueur, message)

@routerf.get("/feed_backs/id_joueur/{identifiant_joueur}", tags=["feed_back"])
def obtenir_tous_ses_feed_backs(identifiant_joueur):
    return FeedBackService.consulter_tous_ses_feedbacks(identifiant_joueur) 
