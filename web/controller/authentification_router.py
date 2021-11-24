from fastapi import APIRouter, Request
from web.service.utilisateur_service import UtilisateurService

router = APIRouter()


@router.get("/utilisateurs/", tags=["utilisateur"])
def obtenir_noms_utilisateurs():
    return UtilisateurService.noms_utilisateurs()

@router.get("/administrateur/{utilisateur_nom}", tags=["utilisateur"])
def utilisateur_admin(utilisateur_nom):
    return UtilisateurService.utilisateur_admin(utilisateur_nom)

@router.get("/utilisateur/{utilisateur_nom}", tags=["utilisateur"])
def existe_utilisateur(utilisateur_nom):
    return UtilisateurService.est_utilisateur(utilisateur_nom)

@router.get("/utilisateur/{utilisateur_nom}/mot_de_passe/{mot_de_passe}", tags=["utilisateur"])
def existe_utilisateur(utilisateur_nom, mot_de_passe):
    return UtilisateurService.verifie_mdp(utilisateur_nom, mot_de_passe)

@router.post("/creation_utilisateur", tags=["utilisateur"])
async def creation_utilisateur(request: Request):
    json_recu = await request.json()
    est_administrateur = json_recu['est_administrateur']
    mot_de_passe = json_recu['mot_de_passe']
    utilisateur_nom = json_recu['utilisateur_nom']
    return UtilisateurService.creation_compte(utilisateur_nom, mot_de_passe, est_administrateur)
