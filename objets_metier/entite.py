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
                       objets: Optional(List[Objet]) = None) -> None: 
        self.__id_joueur = id_joueur
        self.__id_entite = id_entite 
        self.__caracteristiques_entite = caracteristiques_entite
        self.__objets = objets

    @property
    def id_joueur(self):
        return self.__id_joueur

    @id_joueur.setter
    def id_joueur(self, value):
        self.__id_joueur = value
        
    @property
    def id_entite(self):
        return self.__id_entite

    @id_entite.setter
    def id_entite(self, value):
        self.__id_entite = value
    
    @property
    def caracteristiques_entite(self):
        return self.__caracteristiques_entite

    @caracteristiques_entite.setter
    def caracteristiques_entite(self, value):
        self.__caracteristiques_entite = value

    @property
    def objets(self):
        return self.__objets

    @objets.setter
    def objets(self, value):
        self.__objets = value    