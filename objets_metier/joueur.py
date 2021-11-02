from objets_metier.utilisateur import Utilisateur
from objets_metier.personnage import Personnage

class Joueur(Utilisateur):
    """
    Un joueur est un utilisateur qui est présent dans une campagne sans être maître du jeu.
    """
    def __init__(self, personnage : list[Personnage],
                       choix_revelation : bool) : 
        self.__personnage = personnage
        self.__choix_revelation = choix_revelation

    def creer_personnage(self):
        None

    def consulter_personnage(self):
        None

    def modifier_personnage(self):
        None 

    def changer_revelation_jet(self):
        self.__choix_revelation = not(self.__choix_revelation)