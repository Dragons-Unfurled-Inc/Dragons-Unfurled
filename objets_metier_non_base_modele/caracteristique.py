from typing import List, Optional


class Caracteristique : 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    def __init__(self,  nom_entite: str,
                        attaques: List[str],
                        capacites: List[str], 
                        languages: List[str], 
                        description: Optional[str],
                        niveau: int = 1, 
                        experience: int = 20,
                        force: int = 20, 
                        intelligence: int = 20, 
                        charisme: int = 20, 
                        dexterite: int = 20, 
                        constitution: int = 5, 
                        sagesse: int = 20, 
                        vie: int = 10,
                        classe_armure: int = 10) -> None:
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
        self.__classe_armure = classe_armure

    def __str__(self):
        """
        permet un affichage des caractéristiques
        """
        modele = '\n'.join([
            '            Nom : {} \n            Niveau : {} \n            Expérience: {} \n            Force : {} \n            Dextérité : {} \n            Constitution : {} \n            Intelligence : {} \n            Sagesse : {} \n            Charisme : {} \n            Capacités : {} \n            Vie : {} \n            Attaques : {} \n            Langages : {} \n            Description : {} \n            Classe Armure : {}'])
        return modele.format(
            self.__nom_entite,
            self.__niveau,
            self.__experience,
            self.__force,
            self.__dexterite, 
            self.__constitution,
            self.__intelligence,
            self.__sagesse,
            self.__charisme,
            self.__capacites,
            self.__vie,
            self.__attaques,
            self.__languages,
            self.__description,
            self.__classe_armure)
    
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

    @property
    def capacites(self):
        return self.__capacites

    @capacites.setter
    def capacites(self, value):
        self.__capacites = value     

    @property
    def attaques(self):
        return self.__attaques

    @attaques.setter
    def attaques(self, value):
        self.__attaques = value    

    @property
    def languages(self):
        return self.__languages

    @languages.setter
    def languages(self, value):
        self.__languages = value    

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value    

    @property
    def classe_armure(self):
        return self.__classe_armure

    @classe_armure.setter
    def classe_armure(self, value):
        self.__classe_armure = value     