from fastapi import APIRouter
from web.service.joueur_service import JoueurService

routerj = APIRouter()
 

@routerj.get("/joueurs/", tags=["joueur"])
def obtenir_noms_utilisateurs():
    return JoueurService.noms_utilisateurs() 
