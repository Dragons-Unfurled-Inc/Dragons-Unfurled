from random import choice, randint
from typing import List


class Grille:
    """
    Cet objet métier est une grille qui correspond à un espace à deux dimensions dans une salle du donjon.


    ...

    Attributes
    ----------

        largeur : int
                Cette largeur correspond à la distance en abscisse entre la cellule la plus à gauche et celle la plus à droite. 
                Pour une pièce rectangulaire, cette largeur correspond simplement à la largeur de la pièce, murs exclus.

        longueur : int
                De la même manière que pour largeur, longueur correspond à la distance en ordonnée entre la cellule la plus basse et celle la plus haute. 
                Pour une pièce rectangulaire, cette longeur correspond simplement à la longeur de la pièce, murs exclus.

        coordonnees_cellules : List[List[int]]
                C'est la liste des coordonnées des cellules.

        coordonnees_element : List[int]
                Ce sont les coordonnées de l'élément à déplacer. 

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
            Cette fonction permet de dessiner la grille à parir de ses attributs et de la longueur de case choisie.

        dessiner_grille(self, largeur_case = 2) 
            Cette fonction permet de dessiner la grille à parir de ses attributs et de la longueur de case choisie.
    """

    def __init__(self, largeur: int, longueur: int, coordonnees_cellules: list, coordonnees_element: List[int], coordonnees_entites: list, coordonnees_objets: list):
        """
        Une grille s'initialise avec les 6 arguments présentés ci-dessous.


        Parameters
        ----------

            largeur : int
                    Cette largeur correspond à la distance en abscisse entre la cellule la plus à gauche et celle la plus à droite. 
                    Pour une pièce rectangulaire, cette largeur correspond simplement à la largeur de la pièce, murs exclus.

            longueur : int
                    De la même manière que pour largeur, longueur correspond à la distance en ordonnée entre la cellule la plus basse et celle la plus haute. 
                    Pour une pièce rectangulaire, cette longeur correspond simplement à la longeur de la pièce, murs exclus.

            coordonnees_cellules : List[List[int]]
                    C'est la liste des coordonnées des cellules.

            coordonnees_element : List[int]
                    Ce sont les coordonnées de l'élément à déplacer. 

            coordonnees_entites : List[List[int]]
                    C'est la liste des coordonnées des entités dans la pièce.

            coordonnees_objets : List[List[int]]
                    C'est la liste des coordonnées des objets dans la pièce.
        """
        self.largeur = largeur 
        self.longueur = longueur
        self.murs = [] # Cette liste va contenir la lite des coordonnées des murs, une fois placés avec place_murs().
        self.quitter = False # Lorsque quitter passera à True, deplacement_salle_service cessera ses appels à dessiner_grille et deplace_element.
        self.coordonnees_cellules = coordonnees_cellules
        self.coordonnees_objets_non_element = coordonnees_objets
        self.element = coordonnees_element 
        self.coordonnees_entites_non_element = coordonnees_entites  
        if coordonnees_element in self.coordonnees_entites_non_element: # Nous voulons afficher avec un E toutes les entités, sauf l'élement à déplacer. 
            self.coordonnees_entites_non_element.remove(coordonnees_element) 
        if coordonnees_element in self.coordonnees_objets_non_element: # Nous voulons afficher avec un O tous les objets, sauf l'élement à déplacer. 
            self.coordonnees_objets_non_element.remove(coordonnees_element) 

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

        if pos not in self.murs and pos not in self.coordonnees_objets_non_element and pos not in self.coordonnees_entites_non_element: # Nous ne pouvons pas rentrer dans un mur, dans un objet ou un autre entité.
            self.element = pos # La nouvelle position n'est enregistrée, que si la nouvelle position demandée est possible.

    def place_murs_aleatoire(self, pct=.25) -> list: 
        """ 
        Cette fonction permet de remplir aléatoirement la pièce avec un certain pourcentage de murs.
        N.B : Cette fonction n'est pas employée dans la vue de déplacement en donjon. 
        Elle nous a cependant servi à penser nos fonctions et à nous projeter durant l'implémentation du code. 
        Elle donne des résultats satisfaisants, qui pourraient être exploités à postériori.


        Parameters
        ----------
            pct : float
                Cette valeur correspond à la proportion de murs qui vont être générés aléatoirement dans la pièce.
                Rien n'empèche que les murs génés se superposent. 
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
            murs.append([x + choice([-1, 0, 1]), y + choice([-1, 0, 1])]) # La fonction choice choisit au hasard un entier de la liste. 
                                                                          # L'idée est ici de regrouper quelques murs pour un aspect plus réel.
                                                                          # Nous ajoutons donc un mur aléatoirement à une distance en abscisse et ordonnée inférieure ou égale à un du mur précédent.
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
        Cette fonction permet de dessiner la grille à parir de ses attributs et de la longueur de case choisie.


        Parameters
        ----------
            longueur_case: float
                Cette valeur 

        Returns
        -------
            None    
        """
        for y in range(self.longueur + 1, -1, -1): # Nous prenons en compte toutes les cases dans le carré formé par les dimensions de la salle, ainsi que celles sur le contour extérieur.
                                                   # De plus, nous parcourons les rangés de cellules de haut en bas pour que les prints donnent un rendu satisfaisant, avec l'axe des ordonnées orienté vers le haut. 
            for x in range(self.largeur + 2):
                if [x, y] in self.murs:
                    symbol = '#'
                elif [x, y] == self.element:
                    symbol = 'X'
                elif [x, y] in self.coordonnees_entites_non_element:
                    symbol = 'E'
                elif [x, y] in self.coordonnees_objets_non_element:
                    symbol = 'O'
                else:
                    symbol = '.'
                print("%%-%ds" % largeur_case % symbol, end="") # end="" permet de mettre les caractères les uns à la suite des autres, jusqu'à arriver au print en dessous. 
                                                                # De cette manière, nous affichons une ligne de caractères correspondant à une ligne de la grille.
                                                                # Le %d permet d'entrer largeur_case dans l'expréssion (decimal integer) 
                                                                # Le s qui le suit et le 1er % permet de dire que nous sommes en train de spécifier la largeur du print.
                                                                # Le deuxième % sert à insérer le symbole souhaité.
            print()
