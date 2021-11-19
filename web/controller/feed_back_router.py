from fastapi import APIRouter
from objets_metier.utilisateur import Utilisateur
from web.service.feed_back_service import FeedBackService

routerf = APIRouter()
 

@routerf.get("/feed_backs/", tags=["feed_backs"])
def get_noms_feed_backs():
    return FeedBackService.consulter_tous_les_feedbacks()

@routerf.post("/identifiant_joueur/{identifiant_joueur}/message/{message}", tags=["feed_backs"])
def donne_feedback(identifiant_joueur, message):
    FeedBackService.donne_feedback(identifiant_joueur, message)
