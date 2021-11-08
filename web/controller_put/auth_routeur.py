from fastapi import APIRouter
from objets_metier.feedback import Feedback
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.monstre import Monstre
from objets_metier.utilisateur import Utilisateur
from objets_metier.donjon import Donjon
from objets_metier.salle import Salle

from web.service.personnage_service import PersonnageService
from web.service.monstre_service import MonstreService
from web.service.utilisateur_service import UtilisateurService
from web.service.feedback_service import FeedbackService
from web.service.campagne_service import CampagneService
from web.service.donjon_service import DonjonService
from web.service.salle_service import SalleService
# On instancie le webservice

routerput = APIRouter()

caract = Caracteristique("Nom","Attaques", "Capacité", "langages","des")
perso = Personnage("classe","race","lore","id_joueur", "id_entite", "nomentite", caract)

# Défintion du endpoint get /todo
@routerput.put("/personnage")
async def add_personnage(perso:Personnage):
    PersonnageService.add_personnage(perso)
    resultat = perso.dict()
    return resultat

@routerput.put("/monstre")
async def add_personnage(monstre:Monstre):
    MonstreService.add_monstre(monstre)
    resultat = monstre.dict()
    return resultat

@routerput.put("/Utilisateur/{username}")
async def add_personnage(username:str,utili:Utilisateur):
    utilisateur = Utilisateur(utili.connecte, utili.mot_de_passe, username, utili.est_administrateur, utili.feed_backs)
    UtilisateurService.add_utilisateur(utilisateur)
    resultat = {"username": username, **utilisateur.dict()}
    return resultat

# @routerput.put("/Feedback/{username}")
# async def add_feedback(username : str, feed : Feedback):
#     FeedbackService.add_feedback(feed, username)
#     resultat = {"username": username, **feed.dict()}
#     return resultat

@routerput.put("/Campagne")
async def add_campagne(nom_campagne : str):
    id_campagne = CampagneService.add_campagne(nom_campagne)
    return (id_campagne, nom_campagne)

@routerput.put("/Donjon")
async def add_donjon(id_campagne : int, donjon : Donjon):
    DonjonService.add_donjon(id_campagne, donjon)
    return donjon

@routerput.put("/Salle")
async def add_salle(id_donjon : int,salle : Salle) : 
    SalleService.add_salle(id_donjon,salle)
    return salle
