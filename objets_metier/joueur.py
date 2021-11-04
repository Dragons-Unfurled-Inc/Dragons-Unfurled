from typing import List
from pydantic import BaseModel

from objets_metier.utilisateur import Utilisateur
from objets_metier.personnage import Personnage
from objets_metier.feedback import Feedback

class Joueur(Utilisateur, BaseModel):
    """
    Un joueur est un utilisateur qui est présent dans une campagne sans être maître du jeu.
    """
    _personnages : List[Personnage]
    _choix_revelation : bool 

    class Config:
        underscore_attrs_are_private = True

    def __init__(self, personnage : List[Personnage], 
                       connecte : bool,
                       mot_de_passe : str,
                       identifiant : str,
                       est_administrateur : bool, 
                       feed_backs : List[Feedback] = [],
                       choix_revelation : bool = True): 
        self._personnage = personnage
        self._choix_revelation = choix_revelation
        Utilisateur.__init__()


    def creer_personnage(self):
        None

    def consulter_personnage(self, id_campagne):
        None

    def modifier_personnage(self, id_campagne):
        None 

    def changer_revelation_jet(self):
        self._choix_revelation = not(self._choix_revelation)

    @property
    def personnages(self):
        return self._personnages

    @personnages.setter
    def personnages(self, value):
        self._personnages = value

    @property
    def choix_revelation(self):
        return self._choix_revelation

    @choix_revelation.setter
    def choix_revelation(self, value):
        self._choix_revelation = value