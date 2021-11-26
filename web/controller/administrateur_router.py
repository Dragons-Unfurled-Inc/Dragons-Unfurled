from fastapi import APIRouter, Request
from web.service.administrateur_service import AdministrateurService

routera = APIRouter()
 

@routera.patch("/administrateur/termine", tags=["administrateur"])
async def supprimer_droits_administrateur(request: Request):
    administrateur_donneur = await request.json()
    nom_administrateur_donneur = administrateur_donneur['nom']
    AdministrateurService.supprimer_droits_administrateur(nom_administrateur_donneur)  

@routera.patch("/administrateur/nouveau", tags=["administrateur"])
async def ajoute_droits_administrateur(request: Request):
    administrateur_donneur = await request.json()
    nom_administrateur_donneur = administrateur_donneur['nom']
    AdministrateurService.ajouter_droits_administrateur(nom_administrateur_donneur)  

@routera.delete("/bannir/{nom_joueur}", tags=["administrateur"])
def bannir(nom_joueur):
    AdministrateurService.supprimer_compte(nom_joueur)  
