from typing import List
from pydantic import BaseModel
from objets_metier.des import Des

    
class Jet(BaseModel):
    liste_des: List[Des]
    valeur_jet = None
    
    def lancer_des(self):
        self.__valeur_jet = 0
        longueur_liste_des = len(self.__liste_des)
        for i in range(0, longueur_liste_des):
            self.__valeur_jet += self.__liste_des[i].lancer_le_des()
