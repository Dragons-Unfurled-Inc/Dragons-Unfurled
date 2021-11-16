from typing import List
from pydantic import BaseModel
from objets_metier.des import Des

    
class Jet(BaseModel):
    __liste_des: List[Des]
    __valeur_jet = None
    
    class Config:
        underscore_attrs_are_private = True

    def __init__(self, liste_des: List[Des]):
        self.__liste_des = liste_des
        self.__valeur_jet = None

    def lancer_des(self):
        self.__valeur_jet = 0
        longueur_liste_des = len(self.__liste_des)
        for i in range(0, longueur_liste_des):
            self.__valeur_jet += self.__liste_des[i].lancer_le_des()

    @property
    def liste_des(self):
        return self.__liste_des 

    @liste_des.setter
    def liste_des(self, value):
        self.__liste_des = value

    @property
    def valeur_jet(self):
        return self.__valeur_jet

    @valeur_jet.setter
    def valeur_jet(self, value):
        self.__valeur_jet = value