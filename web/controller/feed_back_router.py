from fastapi import APIRouter
from objets_metier.utilisateur import Utilisateur
from web.service.feed_back_service import FeedBackService   

routerf = APIRouter()
 

@routerf.get("/feed_backs/", tags=["feed_backs"])
def get_noms_feed_backs():
    return FeedBackService.consulter_tous_les_feedbacks()

@routerf.get("/administrateur/{utilisateur_nom}", tags=["feed_backs"])
def utilisateur_admin(utilisateur_nom):
    return FeedBackService.utilisateur_admin(utilisateur_nom)

@routerf.get("/utilisateur/{utilisateur_nom}", tags=["feed_backs"])
def existe_utilisateur(utilisateur_nom):
    return FeedBackService.est_utilisateur(utilisateur_nom)

@routerf.get("/utilisateur/{utilisateur_nom}/mot_de_passe/{mot_de_passe}", tags=["feed_backs"])
def existe_utilisateur(utilisateur_nom, mot_de_passe):
    return FeedBackService.verifie_mdp(utilisateur_nom, eval(mot_de_passe))

@routerf.post("/utilisateur/{utilisateur_nom}/mot_de_passe/{mot_de_passe}/est_administrateur/{est_administrateur}", tags=["feed_backs"])
def existe_utilisateur(utilisateur_nom, mot_de_passe, est_administrateur):
    FeedBackService.creation_compte(utilisateur_nom, eval(mot_de_passe), est_administrateur)
