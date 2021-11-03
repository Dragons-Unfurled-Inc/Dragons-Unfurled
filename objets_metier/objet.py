from typing import List, Optional
from pydantic import BaseModel, PrivateAttr

class Objet(BaseModel) : 
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    __id_objet: str = PrivateAttr()
    __nom_objet: str = PrivateAttr()
    __description: str = PrivateAttr()

    def __init__(self,  id_objet: str,
                        nom_objet: str,
                        description: str):
        self.__id_objet = id_objet
        self.__nom_objet = nom_objet
        self.__description = description

    def __str__(self): 
        """
        Affichage des objets
        """
        modele = '\n'.join(['            Identifiant : {} \n            Nom : {} \n            Description : {}'])
        return modele.format(self.__id_objet,
                             self.__nom_objet,
                             self.__description)

    @property
    def id_objet(self):
        return self.__id_objet

    @id_objet.setter
    def id_objet(self, value):
        self.__id_objet = value

    @property
    def nom_objet(self):
        return self.__nom_objet

    @nom_objet.setter
    def nom_objet(self, value):
        self.__nom_objet = value   

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value     
