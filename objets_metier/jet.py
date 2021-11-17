from typing import List

from pydantic import BaseModel

from objets_metier.des import Des


class Jet(BaseModel):
    liste_des: List[Des]
    valeur_jet: int


    def __init__(self, liste_des: List[Des]):
        self.liste_des = liste_des
        self.valeur_jet = None

    def lancer_des(self):
        self.valeur_jet = 0
        longueur_liste_des = len(self.liste_des)
        for i in range(0, longueur_liste_des):
            self.valeur_jet += self.liste_des[i].lancer_le_des()

    