from typing import List, Optional

class Caracteristique :
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    def __init__( self, id_entite: str, 
                        niveau: int = 0, 
                        experience: int = 0
                        force: int = 0, 
                        intelligence: int = 0, 
                        charisme: int = 0, 
                        dexterite: int = 0, 
                        constitution: int = 0, 
                        sagesse: int = 0, 
                        vie: int = 0, 
                        attaques: List[str],
                        capacites: List[str], 
                        languages: List[str], 
                        description: str) -> None:
        self.__id_entite = id_entite
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
    def id_entite(self):
        return self.__id_entite

    @id_entite.setter
    def id_entite(self, value):
        self.__id_entite = value

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
