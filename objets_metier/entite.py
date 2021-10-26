from abc import ABC, abstractmethod

from objets_metier.caracteristique import Caracteristique


class Entite(ABC): 
    def __init__(self, id_joueur, id_entite, nom_entite, objets, caracteristiques = Caracteristique()): #faut trouver un moyen d'initialiser des caracs à chaque fois
        self.id_joueur = id_joueur
        self.id_entite = id_entite  
        self.nom_entite = nom_entite
        self.caracteristiques = caracteristiques
        self.objets = objets
        

    
