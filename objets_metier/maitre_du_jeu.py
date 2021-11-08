from typing import List
from pydantic import BaseModel
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
from objets_metier.donjon import Donjon
from objets_metier.monstre import Monstre
from objets_metier.utilisateur import Utilisateur
from objets_metier.feedback import Feedback
from client.service.monstre_service import MonstreService


class MaitreDuJeu(Joueur,BaseModel):
    __id_campagne : int
    __nom_campagne : str
    __personnages_joueurs : List[Personnage]
    __personnages_non_joueurs : List[Personnage]
    __donjons : List[Donjon]
    __monstres : List[Monstre]
    
    class Config:
        underscore_attrs_are_private = True

    def __init__(self, id_campagne : int,
                       nom_campagne : str,
                       personnage : List[Personnage], 
                       connecte : bool,
                       mot_de_passe : str,
                       identifiant : str,
                       est_administrateur : bool, 
                       feed_backs : List[Feedback] = [],
                       personnages_joueurs : List[Personnage] = [],
                       personnages_non_joueurs : List[Personnage] = [],
                       donjons : List[Donjon] = [],
                       monstres : List[Monstre] = [],
                       choix_revelation : bool = True): 
        self.__id_campagne = id_campagne
        self.__nom_campagne = nom_campagne
        self.__personnages_joueurs = personnages_joueurs
        self.__personnages_non_joueurs = personnages_non_joueurs
        self.__donjons = donjons
        self.__monstres = monstres
        Joueur.__init__(personnage, 
                       connecte,
                       mot_de_passe,
                       identifiant,
                       est_administrateur, 
                       feed_backs,
                       choix_revelation)

    def creer_monstre(self, nom):
        self.__monstres.append(MonstreService.ImportMonstreWeb(nom))
        

    def consulter_monstre(self, monstre : Monstre):
        None

    def liste_joueurs(self):
        liste_joueurs = [] # C'est la liste des identifiants des joueurs.
        liste_personnages = self.personnages_joueurs
        for personnage in liste_personnages:
            liste_joueurs.append(personnage.id_joueur)
        return liste_joueurs

    def trouver_personnage(self,utilisateur_joueur: Joueur): # Cette fonction cherche le personnage d'un utilisateur.
        personnage_joueur = None # C'est le personnage du joueur.
        liste_personnages = utilisateur_joueur.personnages # Les personnages du joueur
        for personnage in liste_personnages:
            if personnage in self.personnages_joueurs:
                personnage_joueur = personnage
        return personnage_joueur

    def modifier_monstre(self, monstre : Monstre):
        None

    def modifier_personnage(self, personnage : Personnage):
        None    

    def ajouter_monstre(self, monstre : Monstre, donjon : Donjon = None): 
       """
       Cette fonction ajoute un monstre dans la campagne. 
       Par défaut l'entité ajoutée ne se trouve pas dans un donjon.
       """
       self.__monstres.append(monstre)
       if donjon != None: 
           donjon.pieces[0].monstres.append(monstre)

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
    def monstres(self):
        return self.__monstres

    @monstres.setter
    def monstres(self, value):
        self.__monstres = value
