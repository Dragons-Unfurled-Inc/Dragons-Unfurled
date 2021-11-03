from abc import ABC, abstractmethod
import copy
from typing import List, Optional

from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet


class Entite(ABC): 
    """
    Une entité est un personnage ou un monstre.
    """ 
    def __init__(self, id_joueur: str, 
                       id_entite: str,                  
                       caracteristiques_entite: Caracteristique,
                       objets: Optional[List[Objet]] = None) -> None: 
        self._id_joueur = id_joueur
        self._id_entite = id_entite 
        self._caracteristiques_entite = caracteristiques_entite
        self._objets = objets

    def __str__(self) : 
        modele = '\n'.join(['Identifiant Joueur : {} \nIdentifiant entité : {} \nCaracteristiques : {} \nObjets : {}'])
        aff_obj = ''
        for obj in self._objets: 
            aff_obj += '\n'
            aff_obj += print(obj)
        return modele.format(self._id_joueur,
                             self._id_entite,
                             print(self._caracteristiques_entite),
                             aff_obj)

    @property
    def id_joueur(self):
        return self._id_joueur

    @id_joueur.setter
    def id_joueur(self, value):
        self._id_joueur = value
        
    @property
    def id_entite(self):
        return self._id_entite

    @id_entite.setter
    def id_entite(self, value):
        self._id_entite = value
    
    @property
    def caracteristiques_entite(self):
        return self._caracteristiques_entite

    @caracteristiques_entite.setter
    def caracteristiques_entite(self, value):
        self._caracteristiques_entite = value

    @property
    def objets(self):
        return self._objets

    @objets.setter
    def objets(self, value):
        self._objets = value    