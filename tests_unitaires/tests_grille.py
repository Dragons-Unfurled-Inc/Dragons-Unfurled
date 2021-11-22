import io
import random
import sys
import unittest
from unittest import TestCase

from objets_metier.grille import Grille


class TestGrille(TestCase):
    """
    Cette classe de tests s'applique à l'objet métier "Grille". Une grille qui correspond à un espace à deux dimension dans une salle du donjon.

    Args:
        TestCase (class): Une classe dont les instances sont des cas de tests unitaires.
    """


    def test_deplace_joueur(self):
        """
        Cette fonction test le déplacement d'un joueur.
        """

        # ETANT DONNÉ
        dimensions = [3,2] # La salle est de largeur 3 et de longueur 2.
        coordonnees_cellules = [[1,2],[2,2],[3,2],[2,1]] # La grille contient quatre cellules. Elles sont placées de manière à former un "T".
        coordonnees_entite = [2, 2] # Le personnage du joueur est sur la cellule du centre.
        coordonnees_entites = [[1, 2],[2,2]] # La salle contient deux entités dont le personnage du joueur.
        coordonnees_objets = [[3, 2]] # La salle contient un objet placé à la droite du joueur.
        grille = Grille(dimensions[0], dimensions[1], coordonnees_cellules, coordonnees_entite, coordonnees_entites, coordonnees_objets) # Nous construisons la grille.

        # SI
        grille.deplace_joueur("b") # Le joueur se déplace vers le bas. 

        # ALORS
        self.assertEqual(grille.joueur,[2,1]) # Le joueur est descendu d'une case.
        self.assertEqual(grille.coordonnees_objets,[[3, 2]]) # L'objet est resté à sa place.
        self.assertEqual(grille.coordonnees_entites_non_joueur,[[1, 2]]) # L'entité qui ne correspondait pas au personnage à déplacer est restée à sa place.
  

    def test_place_murs(self):
        """
        Cette fonciton test la construction de murs.
        """

        # ETANT DONNÉ
        dimensions = [3,2]
        coordonnees_cellules = [[1,2],[2,2],[3,2],[2,1]]
        coordonnees_entite = [2, 2] 
        coordonnees_entites = [[1, 2],[2,2]] 
        coordonnees_objets = [[3, 2]]
        grille = Grille(dimensions[0], dimensions[1], coordonnees_cellules, coordonnees_entite, coordonnees_entites, coordonnees_objets)

        # SI
        grille.place_murs() # Nous plaçons des murs sur un quadrillage taille [5,4] pour en placer tout autour des cellules. 

        # ALORS
        self.assertIn([0,2], grille.murs) # Un mur a été ajouté à gauche de la cellule [1,2].
        self.assertIn([1,1], grille.murs) # Un mur a été ajouté à gauche de la cellule [2,1] et sous la cellule [1,2].
        nombre_de_murs = len(grille.murs)
        self.assertEqual(nombre_de_murs, 16) # Il doit y avoir 5*4 - 4 murs, car il y a 4 cellules.


    def test_dessiner_grille(self): 
        """
        Cette fonction test le dessin de la grille.
        """

        # ETANT DONNÉ
        dimensions = [3,2]
        coordonnees_cellules = [[1,2],[2,2],[3,2],[2,1]]
        coordonnees_entite = [2, 2] 
        coordonnees_entites = [[1, 2],[2,2]] 
        coordonnees_objets = [[3, 2]]
        grille = Grille(dimensions[0], dimensions[1], coordonnees_cellules, coordonnees_entite, coordonnees_entites, coordonnees_objets)
        grille.place_murs()
        capture_du_print = io.StringIO() # Nous créons un objet StringIO.
        sys.stdout = capture_du_print #  Nous redirigeons les prochains prints vers une sauvegarde dans capture_du_print.

        # SI
        grille.dessiner_grille() # Nous dessinons la grille. 

        # ALORS
        sys.stdout = sys.__stdout__ # Nous réinitialisons le fonctionnement de print.
        self.assertEqual(capture_du_print.getvalue(), "# # # # # \n"\
                                                      "# E J O # \n"\
                                                      "# # . # # \n"\
                                                      "# # # # # \n") # L'affichage correspond à la grille que nous venons de concevoir.

            
    def test_place_murs_aleatoire(self):
        """
        Cette fonciton test la construction aléatoire de murs. 
        N.B : Cette fonction n'est pas employée dans la vue de déplacement en donjon. 
        Elle nous a cependant servit à penser nos fonctions et à nous projeter durant l'implémentation du code. 
        Elle donne des résultats satisfaisant, qui pourraient être exploités à postériori.
        """

        # ETANT DONNÉ
        random.seed(1) # Cette graine permet de réobtenir toujours le même résultat. Nous allons donc réaliser un seul exemple de test unitaire possible sur la fonction place_murs_aleatoire.
        dimensions = [2,2] # Nous construison cette fois une salle vide sans entité ni objet.
        coordonnees_cellules = [[1,2],[1,2],[2,1],[2,2]]
        coordonnees_entite = [] 
        coordonnees_entites = [[]] # La liste vide est necessaire dans le cas où il n'y a pas de personnage joueur. 
        coordonnees_objets = []
        grille = Grille(dimensions[0], dimensions[1], coordonnees_cellules, coordonnees_entite, coordonnees_entites, coordonnees_objets)

        # SI
        grille.place_murs_aleatoire(0.5) # Nous plaçons un peu moins de 50% de murs aléatoirement.
        
        # ALORS
        self.assertNotEqual(grille.murs, [])


if __name__ == '__main__':
    unittest.main()
