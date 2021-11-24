from fastapi import APIRouter, Request
from web.service.feed_back_service import FeedBackService

routerf = APIRouter()
 

@routerf.get("/feed_backs/", tags=["feed_back"])
def obtenir_tous_les_feed_backs():
    return FeedBackService.consulter_tous_les_feedbacks()

@routerf.post("/donne_feed_back", tags=["feed_back"])
async def donne_feedback(request: Request):
    json_recu = await request.json()
    identifiant_joueur = json_recu['identifiant_joueur']
    message = json_recu['message']
    FeedBackService.donne_feedback(identifiant_joueur, message)

@routerf.get("/feed_backs/id_joueur/{identifiant_joueur}", tags=["feed_back"])
def obtenir_tous_ses_feed_backs(identifiant_joueur):
    return FeedBackService.consulter_tous_ses_feedbacks(identifiant_joueur) 
