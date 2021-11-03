from typing import List, Optional
from objets_metier.salle import Salle
from pydantic import BaseModel

class Donjon(BaseModel):

    _id_donjon: str
    _nom_donjon: str
    _pieces: Optional[List[Salle]] = None 

    class Config:
        underscore_attrs_are_private = True

    def __str__(self):
        """
        Gère l'affichage des données du donjon
        """  
        mod_salle = '        Vide'
        if self._pieces != None: 
            mod_salle = ''
            curs = len(self._pieces)
            for piece in self._pieces:
                if curs == 1 : 
                    mod_salle += Salle.__str__(piece)
                else :
                    mod_salle += Salle.__str__(piece) + '\n\n'
                    curs -= 1 
        modele = '\n'.join(['id_donjon : {} \nNom : {} \nSalle : \n{} '])
        return modele.format(self._id_donjon, 
                             self._nom_donjon,
                             mod_salle)

    
    def afficher_donjon(self):
        None

    def deplacer_element_salles(self, element:type):
        """
        
        """
        None  

    def ajouter_salle(self, salle : Salle):
        """Cette fonction ajoute une salle au donjon
        """
        if self._pieces == None : 
            self._pieces = [salle]
        else :
            self._pieces.append(salle)

    def editer_salle(self, salle : Salle):
        """
        """
        None    

    def inventaire_donjon(self):
        """
        Renvoies une liste de tous les éléments présents dans le donjon
        """
        inventaire = []
        for salle in self._pieces:
            for objet in salle.objets:
                inventaire.append(objet)
            for entite in salle.entites:
                inventaire.append(entite)
        return inventaire
    
    @property
    def id_donjon(self):
        return self._id_donjon

    @id_donjon.setter
    def id_donjon(self, value):
        self._id_donjon = value   

    @property
    def nom_donjon(self):
        return self.__nom_donjon

    @nom_donjon.setter
    def nom_donjon(self, value):
        self._nom_donjon = value

    @property
    def pieces(self):
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        self._pieces = value  