from typing import List, Optional


class Objet : #Reste à compléter les @ en bas
    """
    Cette classe fait l'inventaire des caractéristiques des entités.
    """
    def __init__(self,  id_objet: str,
                        nom_objet: str,
                        description: str):
        self.__id_objet = id_objet
        self.__nom_objet = nom_objet
        self.__description = description

    @property
    def id_objet(self):
        return self.__id_objet

    @id_objet.setter
    def id_objet(self, value):
        self.__id_objet = value