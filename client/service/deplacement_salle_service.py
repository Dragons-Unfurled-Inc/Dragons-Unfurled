
from objets_metier.grille import Grille


class DeplacementSalleService:

    @staticmethod
    def deplacer_element_dans_salle(dimensions, coordonnees_cellules, coordonnees_element, coordonnees_entites, coordonnees_objets):
        grille = Grille(dimensions[0], dimensions[1], coordonnees_cellules, coordonnees_element, coordonnees_entites, coordonnees_objets) # Nous construisons ici une grille de largeur dimensions[0] et de longueur dimensions[1].
        grille.place_murs() # Nous plaçons des murs autour des cellules de la salle.
        deplacement = ""
        print("Entrez d pour aller à droite, g pour aller à gauche, h pour aller en haut, ou b pour décendre. \nq vous permet de vous arreter à votre position.")
        while deplacement != 'q':
            grille.dessiner_grille()
            deplacement = input("Déplacez-vous ! (d, g, h, b, q)")
            grille.deplace_element(deplacement)
        message = "".join(["Vous voilà placé en position ", str(grille.element)])
        print(message)
        return grille.element
