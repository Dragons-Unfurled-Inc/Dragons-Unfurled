from fastapi import APIRouter
from objets_metier.monstre import Monstre
from web.service.monstre_service import MonstreService

routerm = APIRouter()


@routerm.get("/monstre/{nom_monstre}", tags=["monstre"])
def get_NetMonstre(nom_monstre: str):
    return MonstreService.getNetMonstre(nom_monstre)

@routerm.get("/monstre/{type}", tags=["monstre"])
def get_NetMonstre(type_monstre: str):
    return MonstreService.getNetMonstreDeType(type_monstre)