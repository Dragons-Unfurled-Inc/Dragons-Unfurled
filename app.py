# Import classique
import uvicorn
from fastapi import FastAPI
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.monstre import Monstre
from web.dao.personnage_dao import PersonnageDAO
from web.service.personnage_service import PersonnageService
from web.service.monstre_service import MonstreService

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
    
