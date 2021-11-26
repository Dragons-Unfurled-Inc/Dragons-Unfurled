from fastapi import APIRouter,Query
from web.dao.export_dao import ExportDAO
from web.service.objet_service import ObjetService
from typing import List,Optional
routere = APIRouter()

@routere.get("/table/{table}", tags=["export"])
def SauvegardeTable(table : str):
    return ExportDAO.sauvegarde_table(table)

@routere.get("/tables/contenu/", tags=["export"])
def SauvegardeDB():
    return ExportDAO.sauvegarde_db()

@routere.get("/tables/liste/", tags=["export"])
def ListeDB():
    return ExportDAO.liste_db()

