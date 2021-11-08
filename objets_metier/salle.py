from typing import List, Optional
from pydantic import BaseModel
from objets_metier.objet import Objet
from objets_metier.entite import Entite

class Salle(BaseModel):
    __id_salle: str
    __nom_salle: str
    __coordonnees_salle_donjon: List[int] = [0,0]
    __coordonnees_salle_cellule : List[List[int]] = [[0,0], [1,1]]
    __objets: Optional[List[Objet]] = None
    __entites: Optional[List[Entite]] = None 

    class Config:
        underscore_attrs_are_private = True
        schema_extra = {
            "example": {
                "id_salle" : 3,
                "nom_salle": "salle_essai",
                "coordonnees_salle_donjon" : [0,0],
                "coordonnees_salle_cellule" : [[0,0], [3,2]],
                "objets" : [{
                        "id_objet" : "4", 
                        "nom_objet" : "objet test",
                        "description" : "pioche"
                } ],
                "entite" : None
            }
        } 

    def __init__(self, id_salle: str,
                       nom_salle: str,
                       coordonnees_salle_donjon: List[int] = [0,0],
                       coordonnees_salle_cellule : List[List[int]] =  [[0,0], [1,1]], 
                       objets: Optional[List[Objet]] = None, 
                       entites: Optional[List[Entite]] = None ) -> None:

        self.__id_salle = id_salle
        self.__nom_salle = nom_salle
        self.__coordonnees_salle_donjon = coordonnees_salle_donjon
        self.__coordonnees_salle_cellule = coordonnees_salle_cellule
        self.__objets = objets
        self.__entites = entites

    def __str__(self):
        """
        Gère les données d'affichages des salles 
        """
        aff_obj ='        Vide'
        if self.__objets != None:
            aff_obj = ''
            curs = len(self.__objets)
            for obj in self.__objets: 
                if curs == 1 :
                    aff_obj += Objet.__str__(obj) 
                else: 
                    aff_obj += Objet.__str__(obj) + '\n \n'
                    curs -= 1
        aff_ent ='        Vide'
        if self.__entites != None :
            aff_ent =''
            curs = len(self.__entites)
            for enti in self.__entites: 
                if curs == 1 :
                    aff_ent += Entite.__str__(enti) 
                else : 
                    aff_ent += Entite.__str__(enti) + '\n \n'
                    curs -= 1
        modele = '\n'.join(['    Identifiant : {} \n    Nom : {} \n    Coordonnées donjon : {} \n    Coordonnées cellule : {}\n    Objets : \n{} \n    Entités :\n{}'])
        return modele.format(self.__id_salle,
                             self.__nom_salle,
                             self.__coordonnees_salle_donjon,
                             self.__coordonnees_salle_cellule,
                             aff_obj,
                             aff_ent)


    def inventaire_salle(self):
        None

    def ajouter_entite_salle(self, entite:Entite):
        None 

    def modifier_entite_salle(self, entite:Entite):
        None

    def ajouter_objet(self, objet:Objet):
        None

    def modifier_ojet(self, objet:Objet):
        None

    def editer_salle(self):
        None          

    @property
    def id_salle(self):
        return self.__id_salle

    @id_salle.setter
    def id_salle(self, value):
        self.__id_salle = value   

    @property
    def nom_salle(self):
        return self.__nom_salle

    @nom_salle.setter
    def nom_salle(self, value):
        self.__nom_salle = value

    @property
    def coordonnees_salle_donjon(self):
        return self.__coordonnees_salle_donjon

    @coordonnees_salle_donjon.setter
    def coordonnees(self, value):
        self.__coordonnees_salle_donjon = value   

    @property
    def coordonnees_salle_cellule(self):
        return self.__coordonnees_salle_cellule

    @coordonnees_salle_cellule.setter
    def coordonnees(self, value):
        self.__coordonnees_salle_cellule = value  

    @property
    def objets(self):
        return self.__objets

    @objets.setter
    def objets(self, value):
        self.__objets = value   

    @property
    def entites(self):
        return self.__entites

    @entites.setter
    def entites(self, value):
        self.__entites = value           
