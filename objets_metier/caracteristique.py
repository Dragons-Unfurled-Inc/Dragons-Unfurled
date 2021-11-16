from typing import List, Optional
from pydantic import BaseModel

class Caracteristique(BaseModel) : 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    nom_entite: str 
    attaques: List[str] = []
    capacites: List[str] = []
    languages: List[str] = []
    description: Optional[str] = ''
    niveau: int = 1
    experience: int = 20
    force: int = 20
    intelligence: int = 20
    charisme: int = 20
    dexterite: int = 20 
    constitution: int = 5
    sagesse: int = 20 
    vie: int = 10
    classe_armure: int = 10

    class Config:
        underscore_attrs_are_private = True
        schema_extra = { 
            "example": {
                "nom_entite":"Nom", 
                "attaques":"Attaques", 
                "capacites":"Capacité", 
                "languages":"langages",
                "description":"des", 
                } 
            } 
        
    def __str__(self):
        """
        permet un affichage des caractéristiques
        """
        modele = '\n'.join([
            '            Nom : {} \n            Niveau : {} \n            Expérience: {} \n            Force : {} \n            Dextérité : {} \n            Constitution : {} \n            Intelligence : {} \n            Sagesse : {} \n            Charisme : {} \n            Capacités : {} \n            Vie : {} \n            Attaques : {} \n            Langages : {} \n            Description : {} \n            Classe Armure : {}'])
        return modele.format(
            self.nom_entite,
            self.niveau,
            self.experience,
            self.force,
            self.dexterite, 
            self.constitution,
            self.intelligence,
            self.sagesse,
            self.charisme,
            self.capacites,
            self.vie,
            self.attaques,
            self.languages,
            self.description,
            self.classe_armure)
    
    