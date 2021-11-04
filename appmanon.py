# Import classique
import uvicorn
from fastapi import FastAPI
from objets_metier.personnage import Personnage
from web.dao.personnage_dao import PersonnageDAO

# On instancie le webservice
app = FastAPI()

# Défintion du endpoint get /todo
@app.put("/personnage/")
async def add_personnage(perso:Personnage):
    return perso



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

