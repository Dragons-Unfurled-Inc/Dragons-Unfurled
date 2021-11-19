from fastapi import APIRouter
from objets_metier.utilisateur import Utilisateur
from web.service.utilisateur_service import UtilisateurService

router = APIRouter()


@router.get("/utilisateurs/", tags=["utilisateurs"])
def get_noms_utilisateurs():
    return UtilisateurService.noms_utilisateurs()

@router.get("/administrateur/{utilisateur_nom}", tags=["utilisateurs"])
def utilisateur_admin(utilisateur_nom):
    return UtilisateurService.utilisateur_admin(utilisateur_nom)

@router.get("/utilisateur/{utilisateur_nom}", tags=["utilisateurs"])
def existe_utilisateur(utilisateur_nom):
    return UtilisateurService.est_utilisateur(utilisateur_nom)

@router.get("/utilisateur/{utilisateur_nom}/mot_de_passe/{mot_de_passe}", tags=["utilisateurs"])
def existe_utilisateur(utilisateur_nom, mot_de_passe):
    return UtilisateurService.verifie_mdp(utilisateur_nom, eval(mot_de_passe))

@router.post("/utilisateur/{utilisateur_nom}/mot_de_passe/{mot_de_passe}/est_administrateur/{est_administrateur}", tags=["utilisateurs"])
def existe_utilisateur(utilisateur_nom, mot_de_passe, est_administrateur):
    UtilisateurService.creation_compte(utilisateur_nom, eval(mot_de_passe), est_administrateur)
