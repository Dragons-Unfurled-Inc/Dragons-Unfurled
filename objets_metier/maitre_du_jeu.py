from typing import List

from objets_metier.entite import Entite
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
from objets_metier.donjon import Donjon
from objets_metier.entite import Entite


class MaitreDuJeu(Joueur):
    def __init__(self, id_campagne : int,
                       nom_campagne : str,
                       id_maitre_du_jeu : str, 
                       personnages_joueurs : List[Personnage],
                       personnages_non_joueurs : List[Personnage],
                       donjons : List[Donjon],
                       entites : List[Entite]): 
        self.__id_campagne = id_campagne
        self.__nom_campagne = nom_campagne
        self.__id_maitre_du_jeu = id_maitre_du_jeu
        self.__personnages_joueurs = personnages_joueurs
        self.__personnages_non_joueurs = personnages_non_joueurs
        self.__donjons = donjons
        self.__entites = entites
    
    def creer_entite(self, entite : Entite):
        None

    def consulter_entite(self, entite : Entite):
        None

    def modifier_entite(self, entite : Entite):
        None

    def ajouter_entite(self, entite : Entite, donjon : Donjon): 
       None

    def construire_donjon(self, donjon : Donjon):
       None

    def editer_donjon(self, donjon : Donjon): 
       None        

    @property
    def id_campagne(self):
        return self.__id_campagne

    @id_campagne.setter
    def id_campagne(self, value):
        self.__id_campagne = value

    @property
    def nom_campagne(self):
        return self.__nom_campagne

    @nom_campagne.setter
    def nom_campagne(self, value):
        self.__nom_campagne = value

    @property
    def id_maitre_du_jeu(self):
        return self.__id_maitre_du_jeu

    @id_maitre_du_jeu.setter
    def id_maitre_du_jeu(self, value):
        self.__id_maitre_du_jeu = value

    @property
    def personnages_joueurs(self):
        return self.__personnages_joueurs

    @personnages_joueurs.setter
    def personnages_joueurs(self, value):
        self.__personnages_joueurs = value

    @property
    def personnages_non_joueurs(self):
        return self.__personnages_non_joueurs

    @personnages_non_joueurs.setter
    def personnages_non_joueurs(self, value):
        self.__personnages_non_joueurs = value

    @property
    def donjons(self):
        return self.__donjons

    @donjons.setter
    def donjons(self, value):
        self.__donjons = value

    @property
    def entites(self):
        return self.__entites

    @entites.setter
    def entites(self, value):
        self.__entites = value
