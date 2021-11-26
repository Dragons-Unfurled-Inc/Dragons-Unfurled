from fastapi import APIRouter
from web.service.monstre_service import MonstreService


routerm = APIRouter()


@routerm.get("/monstres/types/{nom_type}", tags=["monstre"])
def get_monstres_de_type(nom_type: str):
    return MonstreService.getNetMonstreDeType(nom_type)

@routerm.get("/monstres/types/", tags=["monstre"])
def get_types_monstres():
    return MonstreService.ImportListeTypes()

@routerm.get("/monstres/{nom_monstre}", tags=["monstre"])
def Creer_monstre(nom_monstre: str):
    return MonstreService.getNetMonstre(nom_monstre)
