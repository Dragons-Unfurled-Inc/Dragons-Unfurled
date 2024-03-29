from objets_metier.grille import Grille


class DeplacementSalleService:

    @staticmethod
    def deplacer_element_dans_salle(dimensions, coordonnees_cellules, coordonnees_element, coordonnees_entites, coordonnees_objets, identifiant_entite = 0, identifiant_salle = 0):
        grille = Grille(dimensions[0], dimensions[1], coordonnees_cellules, coordonnees_element, coordonnees_entites, coordonnees_objets, identifiant_entite, identifiant_salle) # Nous construisons ici une grille de largeur dimensions[0] et de longueur dimensions[1].
        grille.place_murs() # Nous plaçons des murs autour des cellules de la salle.
        deplacement = ""
        while deplacement != 'q':
            with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/donjons/donjon4.txt', 'r', encoding="utf-8") as affichage2:
                print(affichage1.read(),affichage2.read())
            print("\nEntrez d pour aller à droite, g pour aller à gauche, h pour aller en haut, ou b pour décendre. \nr permet de ramasser un objet, a à attaquer le monstre de droite et q sert à vous arreter à votre position.\n")
            grille.dessiner_grille()
            deplacement = input("Déplacez-vous ! (d, g, h, b, r, a, q)")
            grille.deplace_element(deplacement)
        message = "".join(["Vous voilà placé en position ", str(grille.element)])
        print(message)
        return grille.element
