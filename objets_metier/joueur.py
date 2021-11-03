from typing import List
from pydantic import BaseModel
from objets_metier.utilisateur import Utilisateur
from objets_metier.personnage import Personnage

class Joueur(Utilisateur,BaseModel):
    """
    Un joueur est un utilisateur qui est présent dans une campagne sans être maître du jeu.
    """
    personnage : List[Personnage]
    choix_revelation : bool
    
    class Config:
        underscore_attrs_are_private = True

    def creer_personnage(self):
        None

    def consulter_personnage(self):
        None

    def modifier_personnage(self):
        None 

    def changer_revelation_jet(self):
        self.__choix_revelation = not(self.__choix_revelation)

    @property
    def personnage(self):
        return self._personnage

    @personnage.setter
    def personnage(self, value):
        self._personnage = value

    @property
    def choix_revelation(self):
        return self._choix_revelation

    @choix_revelation.setter
    def choix_revelation(self, value):
        self._choix_revelation = value