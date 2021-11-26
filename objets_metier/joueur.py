from pydantic import BaseModel
from web.dao.utilisateur_dao import UtilisateurDAO

from objets_metier.utilisateur import Utilisateur


class Joueur(Utilisateur, BaseModel):
    """
    Un joueur est un utilisateur qui est présent dans une campagne sans être maître du jeu.
    """
    id_campagne: int = -1   
        
    def consulter_personnage(id_campagne, id_utilisateur):
        personnage = UtilisateurDAO.trouver_perso(id_campagne, id_utilisateur)
        print(personnage)

    def changer_revelation_jet(self):
        self._choix_revelation = not(self._choix_revelation)
        