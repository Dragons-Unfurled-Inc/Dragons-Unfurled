from typing import List, Optional

from objets_metier.objet import Objet
from entite import Entite

class Salle:

    def __init__(self, id_salle: str,
                       nom_salle: str,
                       coordonnees_salle: Optional[List[int]] = None,
                       objets: Optional[List[Objet]] = None, 
                       entites: Optional[List[Entite]] = None ) -> None:

        self.__id_salle = id_salle
        self.__nom_salle = nom_salle
        self.__coordonnees_salle = coordonnees_salle
        self.__objets = objets
        self.__entites = entites
    
    def __str__(self):
        """
        Gère les données d'affichages des salles 
        """
        aff_obj ='    Vide'
        if self.__objets != None:
            aff_obj = ''
            for obj in self.__objets: 
                aff_obj += Objet.__str__(obj)
                aff_obj += '  \n'
        aff_ent ='    Vide'
        if self.__entites != None :
            aff_ent =''
            for enti in self.__entites: 
                aff_ent += Entite.__str__(enti)
                aff_ent += '\n'
        modele = '\n'.join(['Identifiant : {} \nNom : {} \nCoordonnées : {} \nObjets : \n{} \nEntités :\n{}'])
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
