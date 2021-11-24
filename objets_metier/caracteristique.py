from typing import Any, List, Optional

from pydantic import BaseModel


class Caracteristique(BaseModel) : 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    nom_entite: str 
    attaques: List[str] = ["Intimidation", "Coup de poing"]
    capacites: List[str] = ["Voir dans le noir", "Double saut"]
    languages: Any = ["Elvish", "Draconic", "Celestial"]
    description: Optional[str] = ''
    niveau: int = 1
    experience: int = 20
    force: int = 20
    intelligence: int = 20
    charisme: int = 20
    dexterite: int = 20 
    constitution: int = 5
    sagesse: int = 20 
    vie: int = 50
    classe_armure: int = 5
    
    def __init__(self,nom_entite: str, 
        attaques: List[str] = ["Intimidation", "Coup de poing"],
        capacites: List[str] = ["Voir dans le noir", "Double saut"],
        languages: Any = ["Elvish", "Draconic", "Celestial"],
        description: Optional[str] = '',
        niveau: int = 1,
        experience: int = 20,
        force: int = 20,
        intelligence: int = 20,
        charisme: int = 20,
        dexterite: int = 20,
        constitution: int = 5,
        sagesse: int = 20,
        vie: int = 50,
        classe_armure: int = 5):
        super().__init__(nom_entite = nom_entite,
            classe_armure = classe_armure,
            force = force,
            dexterite = dexterite,
            constitution = constitution,
            intelligence = intelligence,
            charisme = charisme,
            languages = languages,
            niveau = niveau,
            experience = experience,
            attaques = attaques,
            capacites = capacites,
            description = description,
            sagesse = sagesse,
            vie = vie )
    
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
        
    def str(self):
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
    
    