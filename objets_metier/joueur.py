from typing import List
from pydantic import BaseModel

from objets_metier.utilisateur import Utilisateur
from objets_metier.personnage import Personnage
from objets_metier.feedback import Feedback

class Joueur(Utilisateur, BaseModel):
    """
    Un joueur est un utilisateur qui est présent dans une campagne sans être maître du jeu.
    """
    personnages : List[Personnage]
    choix_revelation : bool 
    
    def creer_personnage(self):
        None

    def consulter_personnage(self, id_campagne):
        None

    def modifier_personnage(self, id_campagne): # Attention, il faut proposer au joueur d'ajouter des objets de l'API dans son inventaire/sa liste d'obj.
        None 

    def changer_revelation_jet(self):
        self._choix_revelation = not(self._choix_revelation)

    # @property
    # def personnages(self):
    #     return self.personnages

    # @personnages.setter
    # def personnages(self, value):
    #      self.personnages = value
    
    # @property
    # def choix_revelation(self):
    #     return self._choix_revelation

    # @choix_revelation.setter
    # def choix_revelation(self, value):
    #     self._choix_revelation = value