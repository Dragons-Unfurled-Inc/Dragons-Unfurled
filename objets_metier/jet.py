import random as rd

class Jet:
    def __init__(self,lanceur,nombre,faces,cible) -> None:
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
        
            