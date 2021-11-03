from typing import List, Optional
from pydantic import BaseModel

class Caracteristique(BaseModel): 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    _nom_entite: str
    _attaques: List[str]
    _capacites: List[str]
    _languages: List[str]
    _description: Optional[str]
    _niveau: int = 1
    _experience: int = 20
    _force: int = 20
    _intelligence: int = 20
    _charisme: int = 20
    _dexterite: int = 20 
    _constitution: int = 5
    _sagesse: int = 20 
    _vie: int = 10
    _classe_armure: int = 10

    class Config:
        underscore_attrs_are_private = True

    def __str__(self):
        """
        permet un affichage des caractéristiques
        """
        modele = '\n'.join([
            '            Nom : {} \n            Niveau : {} \n            Expérience: {} \n            Force : {} \n            Dextérité : {} \n            Constitution : {} \n            Intelligence : {} \n            Sagesse : {} \n            Charisme : {} \n            Capacités : {} \n            Vie : {} \n            Attaques : {} \n            Langages : {} \n            Description : {} \n            Classe Armure : {}'])
        return modele.format(
            self._nom_entite,
            self._niveau,
            self._experience,
            self._force,
            self._dexterite, 
            self._constitution,
            self._intelligence,
            self._sagesse,
            self._charisme,
            self._capacites,
            self._vie,
            self._attaques,
            self._languages,
            self._description,
            self._classe_armure)
    
    @property
    def nom_entite(self):
        return self._nom_entite

    @nom_entite.setter
    def nom_entite(self, value):
        self._nom_entite = value

    @property
    def niveau(self):
        return self._niveau

    @niveau.setter
    def niveau(self, value):
        self._niveau = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, value):
        self._force = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        self._intelligence = value    
        
    @property
    def charisme(self):
        return self._charisme

    @charisme.setter
    def charisme(self, value):
        self._charisme = value   

    @property
    def dexterite(self):
        return self._dexterite

    @dexterite.setter
    def dexterite(self, value):
        self._dexterite = value  

    @property
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, value):
        self._constitution = value   

    @property
    def sagesse(self):
        return self._sagesse

    @sagesse.setter
    def sagesse(self, value):
        self._sagesse = value     

    @property
    def vie(self):
        return self._vie

    @vie.setter
    def vie(self, value):
        self._vie = value      

    @property
    def capacites(self):
        return self._capacites

    @capacites.setter
    def capacites(self, value):
        self._capacites = value     

    @property
    def attaques(self):
        return self._attaques

    @attaques.setter
    def attaques(self, value):
        self._attaques = value    

    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = value    

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value    

    @property
    def classe_armure(self):
        return self._classe_armure

    @classe_armure.setter
    def classe_armure(self, value):
        self._classe_armure = value     