from fastapi import APIRouter
from objets_metier.utilisateur import Utilisateur
from web.service.utilisateur_service import UtilisateurService

router = APIRouter()

@router.post("/utilisateurs/", tags=["utilisateurs"])
def create_utilisateur(identifiant,mot_de_passe,est_admin):
    return UtilisateurService.creation_compte(identifiant,mot_de_passe,est_admin)

# @router.get("/utilisateurs/", tags=["utilisateurs"])
# def get_all_utilisateurs():
#     return UtilisateurService.get_all_utilisateurs()

@router.get("/utilisateurs/", tags=["utilisateurs"])
def get_mdp(utilisateur_nom, mdp):
    return UtilisateurService.verifie_mdp(utilisateur_nom, mdp)

@router.get("/utilisateurs/", tags=["utilisateurs"])
def get_noms_utilisateurs():
    return UtilisateurService.noms_utilisateurs()

# @router.put("/utilisateurs/{utilisateur_name}", tags=["utilisateurs"])
# def update_utilisateur(utilisateur_name: str, utilisateur: Utilisateur):
#     return UtilisateurService.updateUtilisateur(utilisateur_name, utilisateur)

# @router.get("/utilisateurs/{utilisateur_nom}", tags=["utilisateurs_admin"])
# def getUtilisateurAdmin(utilisateur_nom):
#     return UtilisateurService.UtilisateurAdmin(utilisateur_nom)

@router.get("/utilisateurs/{utilisateur_nom}")
def existe_utilisateur(utilisateur_nom):
    return UtilisateurService.est_utilisateur(utilisateur_nom)
