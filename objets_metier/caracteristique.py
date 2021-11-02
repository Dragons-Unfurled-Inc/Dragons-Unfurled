from typing import List, Optional


class Caracteristique : 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    def __init__(self,
                        nom_entite: str,
                        attaques: List[str],
                        capacites: List[str], 
                        languages: List[str], 
                        description: Optional(str),
                        niveau: int = 0, 
                        experience: int = 0,
                        force: int = 0, 
                        intelligence: int = 0, 
                        charisme: int = 0, 
                        dexterite: int = 0, 
                        constitution: int = 0, 
                        sagesse: int = 0, 
                        vie: int = 0) -> None:
        self.__nom_entite = nom_entite
        self.__niveau = niveau 
        self.__experience = experience
        self.__force = force 
        self.__dexterite = dexterite 
        self.__constitution = constitution
        self.__intelligence = intelligence 
        self.__sagesse = sagesse 
        self.__charisme = charisme 
        self.__capacites = capacites
        self.__vie = vie
        self.__attaques = attaques
        self.__languages = languages
        self.__description = description
        self.__experience = experience

    @property
    def nom_entite(self):
        return self.__nom_entite

    @nom_entite.setter
    def nom_entite(self, value):
        self.__nom_entite = value

    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, value):
        self.__niveau = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        self.__experience = value

    @property
    def force(self):
        return self.__force

    @force.setter
    def force(self, value):
        self.__force = value

    @property
    def intelligence(self):
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, value):
        self.__intelligence = value    
        
    @property
    def charisme(self):
        return self.__charisme

    @charisme.setter
    def charisme(self, value):
        self.__charisme = value   

    @property
    def dexterite(self):
        return self.__dexterite

    @dexterite.setter
    def dexterite(self, value):
        self.__dexterite = value  

    @property
    def constitution(self):
        return self.__constitution

    @constitution.setter
    def constitution(self, value):
        self.__constitution = value   

    @property
    def sagesse(self):
        return self.__sagesse

    @sagesse.setter
    def sagesse(self, value):
        self.__sagesse = value     

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, value):
        self.__vie = value            