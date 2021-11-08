# Import classique
import uvicorn
from fastapi import FastAPI
from objets_metier.feedback import Feedback
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.monstre import Monstre
from objets_metier.utilisateur import Utilisateur
from web.service.personnage_service import PersonnageService
from web.service.monstre_service import MonstreService
from web.service.utilisateur_service import UtilisateurService
from web.service.feedback_service import FeedbackService
from web.service.campagne_service import CampagneService

# On instancie le webservice
app = FastAPI()

caract = Caracteristique("Nom","Attaques", "Capacité", "langages","des")
perso = Personnage("classe","race","lore","id_joueur", "id_entite", "nomentite", caract)

# Défintion du endpoint get /todo
@app.put("/personnage")
async def add_personnage(perso:Personnage):
    PersonnageService.add_personnage(perso)
    resultat = perso.dict()
    return resultat

@app.put("/monstre")
async def add_personnage(monstre:Monstre):
    MonstreService.add_monstre(monstre)
    resultat = monstre.dict()
    return resultat

@app.put("/Utilisateur/{username}")
async def add_personnage(username:str,utili:Utilisateur):
    utilisateur = Utilisateur(utili.connecte, utili.mot_de_passe, username, utili.est_administrateur, utili.feed_backs)
    UtilisateurService.add_utilisateur(utilisateur)
    resultat = {"username": username, **utilisateur.dict()}
    return resultat

# @app.put("/Feedback/{username}")
# async def add_feedback(username : str, feed : Feedback):
#     FeedbackService.add_feedback(feed, username)
#     resultat = {"username": username, **feed.dict()}
#     return resultat

@app.put("/campagne")
async def add_campagne(nom_campagne : str):
    CampagneService.add_campagne(nom_campagne)
    return nom_campagne

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
    
