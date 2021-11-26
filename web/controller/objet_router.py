from fastapi import APIRouter
from web.service.objet_service import ObjetService

routero = APIRouter()

@routero.get("/objet/{nom_obj}", tags=["objets"])
def Import_objet(nom_obj: str):
    return ObjetService.getObjet(nom_obj)

@routero.get("/types/objets/", tags=["objets"])
def Import_types():
    return ObjetService.getListTypes()

@routero.get("/objets/type/{nom_obj}", tags=["objets"])
def Type_objet(nom_obj: str):
    return ObjetService.getTypeObjet(nom_obj)

@routero.get("/types/objets/{nom_type}", tags=["objets"])
def Liste_Objets_Type(nom_type: str):
    return ObjetService.getObjetsDeType(nom_type)