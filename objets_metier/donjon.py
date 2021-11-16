from typing import List, Optional
from objets_metier.objet import Objet
from objets_metier.salle import Salle
from pydantic import BaseModel

class Donjon(BaseModel):

    id_donjon: str
    nom_donjon: str
    pieces: Optional[List[Salle]] 

    class Config:
        underscore_attrs_are_private = True
        schema_extra = {
            "example": {
                "id_donjon": 3,
                "nom_donjon": "donjondumythe",
                "pieces": {
                    "id_salle" : 3,
                    "nom_salle" : "salle du mythe",
                    "coordonnees_salle" : [0,0],
                    "objet" : None,
                    "entite" : None
                }
            }
        }

    def __str__(self):
        """
        Gère l'affichage des données du donjon
        """  
        mod_salle = '        Vide'
        if self.__pieces != None: 
            mod_salle = ''
            curs = len(self.pieces)
            for piece in self.pieces:
                if curs == 1 : 
                    mod_salle += Salle.__str__(piece)
                else :
                    mod_salle += Salle.__str__(piece) + '\n\n'
                    curs -= 1 
        modele = '\n'.join(['id_donjon : {} \nNom : {} \nSalle : \n{} '])
        return modele.format(self.id_donjon, 
                             self.nom_donjon,
                             mod_salle)

    
    def afficher_donjon(self):
        print(self)

    def deplacer_element_salles(self, element:type):
        """
        """
        None  

    def ajouter_salle(self, salle : Salle):
        """Cette fonction ajoute une salle au donjon
        """
        if self.pieces == None : 
            self.pieces = [salle]
        else :
            self.pieces.append(salle)

    def editer_salle(self, salle : Salle):
        """
        """
        None    

    def inventaire_donjon(self):
        """
        Renvoies une liste de tous les éléments présents dans le donjon
        """
        inventaire = []
        for salle in self.pieces:
            for objet in salle.objets:
                inventaire.append(objet)
            for entite in salle.entites:
                inventaire.append(entite)
        return inventaire
    
 