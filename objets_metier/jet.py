import random as rd
from typing import List

from objets_metier.des import Des

class Jet:
    def __init__(self, lanceur, 
                       nombre,
                       faces,
                       cible) -> None:
        self.lanceur = lanceur
        self.nombre = nombre 
        self.faces = faces
        self.cible = cible 
        self.resultat = nombre*[0]
        for i in range(nombre) :
            self.resultat[i] = rd.randrange(1,faces)
        
    def __str__(self):
    
        """

        permet un affichage du lancer de dés

        """
        modele = '\n'.join([
            ' Le joueur  {} a lancé  {}  dé(s) à  {} faces et obtenu  {}'])
        return modele.format(
            self.lanceur,
            self.nombre,
            self.faces,
            self.resultat)
        
    def attaquer(self):
        None
    
    def lancer_des(liste_des : List[Des]):
        resultat = 0 
        for i in range(0, len(liste_des)):
            resultat += Des.lancer_un_des(liste_des[i])
        return resultat
