from fastapi import APIRouter
from web.service.monstre_service import MonstreService

routerm = APIRouter()


@routerm.get("monstres/types/{nom_type}", tags=["monstre"])
def get_NetMonstre(nom_type: str):
    return MonstreService.getNetMonstreDeType(nom_type)

@routerm.get("monstres/types", tags=["monstre"])
def get_NetMonstre():
    return MonstreService.ImportListeTypes()

@routerm.post("/monstres/{nom_monstre}", tags=["monstre"])
def Creer_monstre(nom_monstre: str):
    return MonstreService.getNetMonstre(nom_monstre)
