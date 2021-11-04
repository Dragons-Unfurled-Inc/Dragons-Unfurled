# Import classique
import uvicorn
from fastapi import FastAPI
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from web.dao.personnage_dao import PersonnageDAO
from web.service.personnage_service import PersonnageService

# On instancie le webservice
app = FastAPI()

caract = Caracteristique("Nom","Attaques", "Capacité", "langages","des")
perso = Personnage("classe","race","lore","id_joueur", "id_entite", "nomentite", caract)

# Défintion du endpoint get /todo
@app.put("/personnage/{id}")
async def add_personnage(id:int,perso:Personnage):
    PersonnageService.add_personnage(perso)
    resultat = {"id": id, **perso.dict()}
    return resultat

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
    
