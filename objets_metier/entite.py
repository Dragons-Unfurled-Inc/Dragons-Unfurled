from abc import ABC, abstractmethod
from typing import List, Optional
from pydantic import BaseModel
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet


class Entite(ABC, BaseModel): 
    """
    Une entité est un personnage ou un monstre.
    """ 
    id_joueur: str
    id_entite: int
    id_campagne : int                 
    caracteristiques_entite: Caracteristique
    objets: Optional[List[Objet]] = None

    class Config:
        underscore_attrs_are_private = True
        
    def __str__(self) : 
        """
        Affichage d'une entité
        """
        aff_obj = '        Vide'
        if self._objets != None :
            aff_obj = ''
            curs = len(self._objets)
            for obj in self._objets: 
                if curs == 1 : 
                    aff_obj += Objet.__str__(obj)
                else :
                    aff_obj += Objet.__str__(obj) + '\n\n'
                    curs -= 1
        modele = '\n'.join(['        Identifiant Joueur : {} \n        Identifiant entité : {} \n        Caractéristiques : \n{} \n        Objets : \n{}'])
        return modele.format(self._id_joueur,
                             self._id_entite,
                             Caracteristique.__str__(self._caracteristiques_entite),
                             aff_obj)

    