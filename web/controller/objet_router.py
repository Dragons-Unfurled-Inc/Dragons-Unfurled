from fastapi import APIRouter
from web.service.objet_service import ObjetService

routero = APIRouter()

@routero.get("/objet/{nom_objet}", tags=["objets"])
def Import_objet(nom_obj: str):
    return ObjetService.getObjet(nom_obj)

@routero.get("/objet/{nom_objet}", tags=["objets"])
def Import_types(nom_obj: str):
    return ObjetService.getObjet(nom_obj)

routero.get("/objet/{nom_objet}", tags=["objets"])
def Type_objet(nom_obj: str):
    return ObjetService.getObjet(nom_obj)

routero.get("/objet/{nom_objet}", tags=["objets"])
def Liste_types(nom_obj: str):
    return ObjetService.getObjet(nom_obj)