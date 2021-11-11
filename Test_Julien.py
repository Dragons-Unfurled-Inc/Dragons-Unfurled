from random import randint, choice
import subprocess, time, platform


class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.mures = []
        self.joueur = (0, 0)
        self.quitter = False

    def deplace_joueur(self, deplacement):
        x = self.joueur[0]
        y = self.joueur[1]
        pos = None

        if deplacement[0] == 'd':
            pos = (x + 1, y)
        elif deplacement[0] == 'g':
            pos = (x - 1, y)
        elif deplacement[0] == 'h':
            pos = (x, y - 1)
        elif deplacement[0] == 'b':
            pos = (x, y + 1)
        else:
            pos = (x, y)
            self.joueur = pos

        if pos not in self.mures and pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.largeur and pos[0] < self.hauteur: # Si on rentre dans un mur.
            self.joueur = pos

def dessiner_grille(g, largeur=2):
    for y in range(g.hauteur):
        for x in range(g.largeur):
            if (x, y) in g.mures:
                symbol = '#'
            elif (x, y) == g.joueur:
                symbol = 'J'
            else:
                symbol = '.'
            print("%%-%ds" % largeur % symbol, end="")
        print()

def place_mures(g: Grille, pct=.25) -> list:
        sortie = []
        for i in range(int(g.hauteur*g.largeur*pct)//2):

            x = randint(1, g.largeur-2)
            y = randint(1, g.hauteur-2)

            sortie.append((x, y))
            sortie.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
        return sortie

# def nettoyer():
#     subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
#     time.sleep(.1)


def main():
    g = Grille(20, 10)
    g.mures = place_mures(g)
    deplacement = "t"
    print("Entrez d pour aller à droite, g pour aller à gauche, h pour aller en haut, ou b pour décendre. \nq vous permet de vous arreter à votre position.")
    while deplacement[0] != 'q':
        dessiner_grille(g)
        deplacement = input("Déplacez-vous ! (d, g, h, b, q)")
        g.deplace_joueur(deplacement)
        # nettoyer() # Cette fonction devrait permettre d'effacer les grilles précedentes.
    message = "".join(["Vous voilà placé en position ", str(g.joueur)])
    print(message)


if __name__ == '__main__':
    main()