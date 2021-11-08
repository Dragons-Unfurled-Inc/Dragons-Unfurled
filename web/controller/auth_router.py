from fastapi import APIRouter
from client.service.monstre_service import MonstreService

router = APIRouter()

@router.get("/monstres/{nom_monstre}")
def Creer_monstre(nom_monstre: str):
    return MonstreService.ImportMonstreWeb(nom_monstre)



