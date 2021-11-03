from typing import List, Optional
from pydantic import BaseModel
from objets_metier.objet import Objet
from objets_metier.entite import Entite

class Salle(BaseModel):
    id_salle: str
    nom_salle: str
    coordonnees_salle: Optional[List[int]] = None
    objets: Optional[List[Objet]] = None
    entites: Optional[List[Entite]] = None 

    class Config:
        underscore_attrs_are_private = True

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
        modele = '\n'.join(['    Identifiant : {} \n    Nom : {} \n    Coordonnées : {} \n    Objets : \n{} \n    Entités :\n{}'])
        return modele.format(self.__id_salle,
                             self.__nom_salle,
                             self.__coordonnees_salle,
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
    def coordonnees_salle(self):
        return self.__coordonnees_salle

    @coordonnees_salle.setter
    def coordonnees(self, value):
        self.__coordonnees_salle = value   

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
