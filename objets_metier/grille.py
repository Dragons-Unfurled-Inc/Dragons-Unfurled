from random import choice, randint
import unittest

class Grille:

    def __init__(self, largeur, longueur, coordonnees_cellules, coordonnees_entite, coordonnees_entites, coordonnees_objets):
        self.largeur = largeur
        self.longueur = longueur
        self.murs = []
        self.joueur = coordonnees_entite
        self.quitter = False
        self.coordonnees_cellules = coordonnees_cellules
        self.coordonnees_entite = coordonnees_entite
        self.coordonnees_entites = coordonnees_entites
        self.coordonnees_objets = coordonnees_objets

    def deplace_joueur(self, deplacement):
        x = self.joueur[0]
        y = self.joueur[1]
        pos = None

        if deplacement == 'd':
            pos = [x + 1, y]
        elif deplacement == 'g':
            pos = [x - 1, y]
        elif deplacement == 'h':
            pos = [x, y - 1]
        elif deplacement == 'b':
            pos = [x, y + 1]
        else:
            pos = [x, y]
            self.joueur = pos

        if pos not in self.murs and pos not in self.coordonnees_objets and pos not in self.coordonnees_entites: # Nous ne pouvons pas rentrer dans un mur, dans un objet ou un autre entité.
            self.joueur = pos

    def place_murs_aleatoire(self, pct=.25) -> list: # pct est le pourcentage de murs que nous voulons rajouter
            murs = []
            for i in range(int(self.longueur*self.largeur*pct)//2):

                x = randint(1, self.largeur-2)
                y = randint(1, self.longueur-2)

                murs.append([x, y])
                murs.append([x + choice([-1, 0, 1]), y + choice([-1, 0, 1])]) # La fonction choice choisie au hasard un entier de la liste. L'idée est ici de regrouper quelques murs pour un aspect plus réel.
            self.murs = murs

    def place_murs(self) -> list:
            murs = []
            for x in range(self.largeur + 2):
                for y in range(self.longueur + 2):
                    if [x,y] not in self.coordonnees_cellules:
                        murs.append([x, y]) # Nous rajoutons des murs à chaque endroit où il n'y a pas de cellule.
            self.murs = murs

    def dessiner_grille(self, largeur_case = 2): 
        for y in range(self.longueur + 2):
            for x in range(self.largeur + 2):
                if [x, y] in self.murs:
                    symbol = '#'
                elif [x, y] == self.joueur:
                    symbol = 'J'
                elif [x, y] in self.coordonnees_entites:
                    symbol = 'E'
                elif [x, y] in self.coordonnees_objets:
                    symbol = 'O'
                else:
                    symbol = '.'
                print("%%-%ds" % largeur_case % symbol, end="")
            print()

if __name__ == '__main__':
    from client.service.deplacement_salle_service import \
        DeplacementSalleService
    DeplacementSalleService.deplacer_entite_dans_salle(dimensions = [30,14], 
                                                       coordonnees_cellules = [[2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [9, 9], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14], [11, 9], [11, 10], [11, 11], [11, 12], [11, 13], [11, 14], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [13, 14], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [17, 9], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [18, 9], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [21, 9], [21, 10], [21, 11], [21, 12], [21, 13], [21, 14], [22, 9], [22, 10], [22, 11], [22, 12], [22, 13], [22, 14], [23, 9], [23, 10], [23, 11], [23, 12], [23, 13], [23, 14], [24, 9], [24, 10], [24, 11], [24, 12], [24, 13], [24, 14], [25, 9], [25, 10], [25, 11], [25, 12], [25, 13], [25, 14], [26, 9], [26, 10], [26, 11], [26, 12], [26, 13], [26, 14], [27, 9], [27, 10], [27, 11], [27, 12], [27, 13], [27, 14], [28, 9], [28, 10], [28, 11], [28, 12], [28, 13], [28, 14], [29, 9], [29, 10], [29, 11], [29, 12], [29, 13], [29, 14], [14, 5], [14, 6], [14, 7], [14, 8], [15, 5], [15, 6], [15, 7], [15, 8], [16, 5], [16, 6], [16, 7], [16, 8], [17, 5], [17, 6], [17, 7], [17, 8], [21, 1], [21, 2], [21, 3], [21, 4], [21, 5], [21, 6], [22, 1], [22, 2], [22, 3], [22, 4], [22, 5], [22, 6], [23, 1], [23, 2], [23, 3], [23, 4], [23, 5], [23, 6], [24, 1], [24, 2], [24, 3], [24, 4], [24, 5], [24, 6], [25, 1], [25, 2], [25, 3], [25, 4], [25, 5], [25, 6], [26, 1], [26, 2], [26, 3], [26, 4], [26, 5], [26, 6], [27, 1], [27, 2], [27, 3], [27, 4], [27, 5], [27, 6], [28, 1], [28, 2], [28, 3], [28, 4], [28, 5], [28, 6], [29, 1], [29, 2], [29, 3], [29, 4], [29, 5], [29, 6], [30, 1], [30, 2], [30, 3], [30, 4], [30, 5], [30, 6], [11, 3], [11, 4], [12, 3], [12, 4], [13, 3], [13, 4], [14, 3], [14, 4], [15, 3], [15, 4], [16, 3], [16, 4], [17, 3], [17, 4], [18, 3], [18, 4], [19, 3], [19, 4], [20, 3], [20, 4], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6]],
                                                       coordonnees_entite = [1, 1],
                                                       coordonnees_entites = [[2,2], [27,11], [15, 10],[16,10],[8,4],[22,4],[6, 11], [9, 11], [10, 11], [11, 11], [14, 11], [15, 11], [16, 11], [17, 11], [20, 11], [21, 11], [22, 11], [25, 11]],
                                                       coordonnees_objets = [[15,3], [19,9], [29,2], [2, 14], [3, 14], [4, 14], [15, 14], [16, 14], [27, 14], [28, 14], [29, 14]])
