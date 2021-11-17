from typing import List, Optional
from pydantic import BaseModel
from objets_metier.objet import Objet
from objets_metier.entite import Entite

class Salle(BaseModel):
    id_salle: str
    nom_salle: str
    coordonnees_salle_donjon: List[int] = [0,0]
    coordonnees_salle_cellule : List[List[int]] = [[0,0], [1,1]]
    objets: Optional[List[Objet]] = None
    entites: Optional[List[Entite]] = None 

    class Config:
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
        
    def __str__(self):
        """
        Gère les données d'affichages des salles 
        """
        aff_obj ='        Vide'
        if self.objets != None:
            aff_obj = ''
            curs = len(self.objets)
            for obj in self.objets: 
                if curs == 1 :
                    aff_obj += Objet.__str__(obj) 
                else: 
                    aff_obj += Objet.__str__(obj) + '\n \n'
                    curs -= 1
        aff_ent ='        Vide'
        if self.entites != None :
            aff_ent =''
            curs = len(self.entites)
            for enti in self.entites: 
                if curs == 1 :
                    aff_ent += Entite.__str__(enti) 
                else : 
                    aff_ent += Entite.__str__(enti) + '\n \n'
                    curs -= 1
        modele = '\n'.join(['    Identifiant : {} \n    Nom : {} \n    Coordonnées donjon : {} \n    Coordonnées cellule : {}\n    Objets : \n{} \n    Entités :\n{}'])
        return modele.format(self.id_salle,
                             self.nom_salle,
                             self.coordonnees_salle_donjon,
                             self.coordonnees_salle_cellule,
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

