from random import choice, randint
from typing import List


class Grille:
    """
    Cet objet métier est une grille qui correspond à un espace à deux dimension dans une salle du donjon.


    ...

    Attributes
    ----------

        largeur : int
                Cette largeur correspond à la distance en abscice entre la cellule la plus à gauche et celle la plus à droite. 
                Pour une pièce rectangulaire, cette largeur correspond simplement à la largeur de la pièce, murs exclus.

        longueur : int
                De la même manière que pour largeur, longueur correspond à la distance en ordonnée entre la cellule la plus basse et celle la plus haute. 
                Pour une pièce rectangulaire, cette longeur correspond simplement à la longeur de la pièce, murs exclus.

        coordonnees_cellules : List[List[int]]
                C'est la liste des coordonnées des cellules.

        coordonnees_element : List[int]
                Ce sont les coordonnées de l'element à déplacer. 

        coordonnees_entites : List[List[int]]
                C'est la liste des coordonnées des entités dans la pièce.

        coordonnees_objets : List[List[int]]
                C'est la liste des coordonnées des objets dans la pièce.


    Methods
    -------

        deplace_element(self, deplacement)
            Cette fonction permet de déplacer l'élément ou de terminer son déplacement.

        place_murs_aleatoire(self, pct=.25)
            Cette fonction permet de remplir aléatoirement la pièce avec un certain pourcentage de murs.

        place_murs(self)
            Cette fonction permet de placer les murs dans la pièce.

        dessiner_grille(self, largeur_case = 2) 
            Cette fonction permet de déssiner la grille à parir de ses attributs et de la longueur de case choisie.

        dessiner_grille(self, largeur_case = 2) 
            Cette fonction permet de déssiner la grille à parir de ses attributs et de la longueur de case choisie.
    """

    def __init__(self, largeur: int, longueur: int, coordonnees_cellules: list, coordonnees_element: List[int], coordonnees_entites: list, coordonnees_objets: list):
        """
        Une grille s'initialise avec les 6 arguments présentés ci-dessous.


        Parameters
        ----------

            largeur : int
                    Cette largeur correspond à la distance en abscice entre la cellule la plus à gauche et celle la plus à droite. 
                    Pour une pièce rectangulaire, cette largeur correspond simplement à la largeur de la pièce, murs exclus.

            longueur : int
                    De la même manière que pour largeur, longueur correspond à la distance en ordonnée entre la cellule la plus basse et celle la plus haute. 
                    Pour une pièce rectangulaire, cette longeur correspond simplement à la longeur de la pièce, murs exclus.

            coordonnees_cellules : List[List[int]]
                    C'est la liste des coordonnées des cellules.

            coordonnees_element : List[int]
                    Ce sont les coordonnées de l'element à déplacer. 

            coordonnees_entites : List[List[int]]
                    C'est la liste des coordonnées des entités dans la pièce.

            coordonnees_objets : List[List[int]]
                    C'est la liste des coordonnées des objets dans la pièce.
        """
        self.largeur = largeur 
        self.longueur = longueur
        self.murs = [] # Cette liste va contenir la lite des coordonnées des murs, une fois placés avec place_murs().
        self.quitter = False # Lorsque quitter passera à True, deplacement_salle_service cessera ses appels à la déssiner_grille et déplace_element.
        self.coordonnees_cellules = coordonnees_cellules
        self.coordonnees_objets = coordonnees_objets
        self.element = coordonnees_element 
        self.coordonnees_entites_non_element = coordonnees_entites # Nous ne voulons afficher avec un E toutes les entités, sauf l'élement à déplacer. 
        self.coordonnees_entites_non_element.remove(coordonnees_element) 

    def deplace_element(self, deplacement):
        """ 
        Cette fonction permet de déplacer l'élément ou de terminer son déplacement.


        Parameters
        ----------
            deplacement : str
                Déplacement correspond à une lettre permettant de déplacer l'élément dans la bonne direction, ou à "q" pour terminer le déplacement. 
                "d" permet d'aller à droite.
                "g" permet d'aller à gauche.
                "h" permet d'aller vers le haut.
                "b" permet d'aller vers le bas.
                "q" permet de terminer le déplacement.

        Returns
        -------
            None
        """
        x = self.element[0] # Nous récupérons ici les coordonnées de l'élément.
        y = self.element[1]
        pos = None # pos correspondera à la prochaine position de l'élément.

        if deplacement == 'd': # La nouvelle position s'enregistre comme souhaité.
            pos = [x + 1, y]
        elif deplacement == 'g':
            pos = [x - 1, y]
        elif deplacement == 'h':
            pos = [x, y + 1]
        elif deplacement == 'b':
            pos = [x, y - 1]
        else:
            pos = [x, y]
            self.element = pos # Si le message entré ne convient pas, la position ne change pas.

        if pos not in self.murs and pos not in self.coordonnees_objets and pos not in self.coordonnees_entites_non_element: # Nous ne pouvons pas rentrer dans un mur, dans un objet ou un autre entité.
            self.element = pos # La nouvelle position n'est enregistré, que si la nouvelle position demandée est possible.

    def place_murs_aleatoire(self, pct=.25) -> list: 
        """ 
        Cette fonction permet de remplir aléatoirement la pièce avec un certain pourcentage de murs.
        N.B : Cette fonction n'est pas employée dans la vue de déplacement en donjon. 
        Elle nous a cependant servit à penser nos fonctions et à nous projeter durant l'implémentation du code. 
        Elle donne des résultats satisfaisant, qui pourraient être exploités à postériori.


        Parameters
        ----------
            pct : float
                Cette valeur correspond à la proportion de murs qui vont être généré aléatoirement dans la pièce.
                Rien n'empèche que les murs géné se superpose. 
                Ceci n'est pas un problème, mais est bon à savoir. 
                Il y aura donc un peu moins de pct*100% de murs dans la pièce.

        Returns
        -------
            None    
        """
        murs = [] # Cette liste va se remplir avec les coordonnées des murs.
        for _ in range(int(self.longueur*self.largeur*pct)//2): # Nous longueur*largeur donne le nombre de murs dans la pièce. 
                                                                # Nous multiplions par pct et prenons la partie entière pour avoir le pourcentage de murs voulu. 
                                                                # Enfin, nous prenons le quotient de la division par 2 car nous allons faire deux génération à chaque itération.

            x = randint(1, self.largeur+1) # Nous générons la position d'un prochain mur aléatoirement.
            y = randint(1, self.longueur+1)

            murs.append([x, y]) # Nous ajoutons le mur.
            murs.append([x + choice([-1, 0, 1]), y + choice([-1, 0, 1])]) # La fonction choice choisie au hasard un entier de la liste. 
                                                                          # L'idée est ici de regrouper quelques murs pour un aspect plus réel.
                                                                          # Nous ajoutons donc un mur aléatoirement à une distance en abscisse et ordonnée inférieur ou égale à un du mur précédent.
        self.murs = murs

    def place_murs(self) -> list:
        """ 
        Cette fonction permet de placer les murs dans la pièce.


        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        murs = [] # Cette liste va se remplir avec les coordonnées des murs.
        for x in range(self.largeur + 2): # Nous prenons en compte toutes les cases dans le carré formé par les dimensions de la salle, ainsi que celle sur le contour extérieur, pour qu'il n'y ai pas d'échappatoire.
            for y in range(self.longueur + 2):
                if [x,y] not in self.coordonnees_cellules:
                    murs.append([x, y]) # Nous rajoutons des murs à chaque endroit où il n'y a pas de cellule.
        self.murs = murs

    def dessiner_grille(self, largeur_case = 2): 
        """ 
        Cette fonction permet de déssiner la grille à parir de ses attributs et de la longueur de case choisie.


        Parameters
        ----------
            longueur_case: float
                Cette valeur 

        Returns
        -------
            None    
        """
        for y in range(self.longueur + 1, -1, -1): # Nous prenons en compte toutes les cases dans le carré formé par les dimensions de la salle, ainsi que celle sur le contour extérieur.
                                                   # De plus, nous parcourons les rangés de cellules de haut en bas pour que les prints donne un rendu satisfaisant, avec l'axe des ordonnées orienté vers le haut. 
            for x in range(self.largeur + 2):
                if [x, y] in self.murs:
                    symbol = '#'
                elif [x, y] == self.element:
                    symbol = 'X'
                elif [x, y] in self.coordonnees_entites_non_element:
                    symbol = 'E'
                elif [x, y] in self.coordonnees_objets:
                    symbol = 'O'
                else:
                    symbol = '.'
                print("%%-%ds" % largeur_case % symbol, end="") # end="" permet de mettre les caractères les uns à la suite des autres, jusqu'à arriver au print en dessous. 
                                                                # De cette manière, nous affichons une ligne de caractères correspondant à une ligne de la grille.
                                                                # Le %d permet d'entrer largeur_case dans l'expréssion (decimal integer) 
                                                                # Le s qui le suit et le 1er % permet de dire que nous somme en train de spécifier la largeur du print.
                                                                # Le deuxième % sert à insérer le symbol souhaité.
            print()

if __name__ == '__main__':
    from client.service.deplacement_salle_service import \
        DeplacementSalleService
    DeplacementSalleService.deplacer_entite_dans_salle(dimensions = [30,14], 
                                                       coordonnees_cellules = [[2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [9, 9], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14], [11, 9], [11, 10], [11, 11], [11, 12], [11, 13], [11, 14], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [13, 14], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [17, 9], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [18, 9], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [21, 9], [21, 10], [21, 11], [21, 12], [21, 13], [21, 14], [22, 9], [22, 10], [22, 11], [22, 12], [22, 13], [22, 14], [23, 9], [23, 10], [23, 11], [23, 12], [23, 13], [23, 14], [24, 9], [24, 10], [24, 11], [24, 12], [24, 13], [24, 14], [25, 9], [25, 10], [25, 11], [25, 12], [25, 13], [25, 14], [26, 9], [26, 10], [26, 11], [26, 12], [26, 13], [26, 14], [27, 9], [27, 10], [27, 11], [27, 12], [27, 13], [27, 14], [28, 9], [28, 10], [28, 11], [28, 12], [28, 13], [28, 14], [29, 9], [29, 10], [29, 11], [29, 12], [29, 13], [29, 14], [14, 5], [14, 6], [14, 7], [14, 8], [15, 5], [15, 6], [15, 7], [15, 8], [16, 5], [16, 6], [16, 7], [16, 8], [17, 5], [17, 6], [17, 7], [17, 8], [21, 1], [21, 2], [21, 3], [21, 4], [21, 5], [21, 6], [22, 1], [22, 2], [22, 3], [22, 4], [22, 5], [22, 6], [23, 1], [23, 2], [23, 3], [23, 4], [23, 5], [23, 6], [24, 1], [24, 2], [24, 3], [24, 4], [24, 5], [24, 6], [25, 1], [25, 2], [25, 3], [25, 4], [25, 5], [25, 6], [26, 1], [26, 2], [26, 3], [26, 4], [26, 5], [26, 6], [27, 1], [27, 2], [27, 3], [27, 4], [27, 5], [27, 6], [28, 1], [28, 2], [28, 3], [28, 4], [28, 5], [28, 6], [29, 1], [29, 2], [29, 3], [29, 4], [29, 5], [29, 6], [30, 1], [30, 2], [30, 3], [30, 4], [30, 5], [30, 6], [11, 3], [11, 4], [12, 3], [12, 4], [13, 3], [13, 4], [14, 3], [14, 4], [15, 3], [15, 4], [16, 3], [16, 4], [17, 3], [17, 4], [18, 3], [18, 4], [19, 3], [19, 4], [20, 3], [20, 4], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6]],
                                                       coordonnees_element = [1, 1],
                                                       coordonnees_entites = [[1, 1], [2,2], [27,11], [15, 10],[16,10],[8,4],[22,4],[6, 11], [9, 11], [10, 11], [11, 11], [14, 11], [15, 11], [16, 11], [17, 11], [20, 11], [21, 11], [22, 11], [25, 11]],
                                                       coordonnees_objets = [[15,3], [19,9], [29,2], [2, 14], [3, 14], [4, 14], [15, 14], [16, 14], [27, 14], [28, 14], [29, 14]])
