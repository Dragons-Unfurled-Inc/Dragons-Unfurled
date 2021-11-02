from typing import List

from objets_metier.entite import Entite
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
#from objets_metier.donjon import Donjon
from objets_metier.entite import Entite


class MaitreDuJeu(Joueur):
    def __init__(self, id_campagne : int,
                       nom_campagne : str,
                       id_maitre_du_jeu : str, 
                       personnages_joueurs : List[Personnage],
                       personnages_non_joueurs : List[Personnage],
#                       donjons : list[Donjons]
                       entites : List[Entite]): 
        self.__id_campagne = id_campagne
        self.__nom_campagne = nom_campagne
        self.__id_maitre_du_jeu = id_maitre_du_jeu
        self.__personnage_joueurs = personnages_joueurs
        self.__personnage_non_joueurs = personnages_non_joueurs
#        self.__donjons = donjons
        self.__entites = entites
    
    def creer_entite(self, entite : Entite):
        None

    def consulter_entite(self, entite : Entite):
        None

    def modifier_entite(self, entite : Entite):
        None

#    def ajouter_entite(self, entite : Entite, donjon : Donjon): 
#       None

#    def construire_donjon(self, donjon : Donjon):
#       None

#    def editer_donjon(self, donjon : Donjon): 
#       None        