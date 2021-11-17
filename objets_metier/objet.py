from typing import List, Optional
from pydantic import BaseModel, PrivateAttr

class Objet(BaseModel) : 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    id_objet: str 
    nom_objet: str 
    description_obj: str
        
    def __str__(self): 
        """
        Affichage des objets
        """
        modele = '\n'.join(['            Identifiant : {} \n            Nom : {} \n            Description : {}'])
        return modele.format(self.id_objet,
                             self.nom_objet,
                             self.description_obj)
