from typing import List
from pydantic import BaseModel
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
from objets_metier.donjon import Donjon
from objets_metier.monstre import Monstre
from objets_metier.utilisateur import Utilisateur
from objets_metier.feedback import FeedBack
from client.service.monstre_service import MonstreService


class MaitreDuJeu(Joueur,BaseModel):
    
    id_campagne : int
    
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