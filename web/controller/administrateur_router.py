from fastapi import APIRouter
from objets_metier.utilisateur import Utilisateur
from web.service.administrateur_service import AdministrateurService

routera = APIRouter()
 

@routera.patch("/administrateur/termine/{nom_administrateur_donneur}", tags=["feed_backs"])
def supprimer_droits_administrateur(nom_administrateur_donneur):
    return AdministrateurService.supprimer_droits_administrateur(nom_administrateur_donneur)  

@routera.patch("/administrateur/nouveau/{nom_administrateur_donneur}", tags=["feed_backs"])
def ajoute_droits_administrateur(nom_administrateur_donneur):
    return AdministrateurService.ajouter_droits_administrateur(nom_administrateur_donneur)  

@routera.delete("/bannir/{nom_joueur}", tags=["feed_backs"])
def bannir(nom_joueur):
    return AdministrateurService.supprimer_compte(nom_joueur)  
