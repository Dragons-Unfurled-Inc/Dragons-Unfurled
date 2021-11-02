from typing import List, Optional
from objets_metier.salle import Salle


class Donjon():

    def __init__(self,
                    id_donjon: str,
                    nom_donjon: str,
                    pieces: Optional[List[Salle]] = None ) -> None:
        
        self.__id_donjon = id_donjon
        self.__nom_donjon = nom_donjon
        self.__pieces = pieces
    
    @property
    def id_donjon(self):
        return self.__id_donjon

    @id_donjon.setter
    def id_donjon(self, value):
        self.__id_donjon = value   

    @property
    def nom_donjon(self):
        return self.__nom_donjon

    @nom_donjon.setter
    def nom_donjon(self, value):
        self.__nom_donjon = value

    @property
    def pieces(self):
        return self.__pieces

    @pieces.setter
    def pieces(self, value):
        self.__pieces = value        

    def afficher_donjon(self):
        None 

    def deplacer_element_salles(self, element:type):
        None  

    def ajouter_salle(self, salle:type):
        None

    def editer_salle(self, salle:type):
        None    

    def inventaire_donjon(self):
        None    