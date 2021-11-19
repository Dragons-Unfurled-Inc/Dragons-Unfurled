from typing import List
from pydantic import BaseModel

from objets_metier.utilisateur import Utilisateur
from objets_metier.personnage import Personnage
from objets_metier.feedback import FeedBack

from web.dao.utilisateur_dao import UtilisateurDAO

class Joueur(Utilisateur, BaseModel):
    """
    Un joueur est un utilisateur qui est présent dans une campagne sans être maître du jeu.
    """
    id_campagne: int = -1 
    
    def ajouter_personnage(self):
        None
        
    def consulter_personnage(id_campagne, id_utilisateur):
        personnage = UtilisateurDAO.trouver_perso(id_campagne, id_utilisateur)
        print(personnage)

    def modifier_personnage(self, id_campagne): # Attention, il faut proposer au joueur d'ajouter des objets de l'API dans son inventaire/sa liste d'obj.
        None 

    def changer_revelation_jet(self):
        self._choix_revelation = not(self._choix_revelation)
        