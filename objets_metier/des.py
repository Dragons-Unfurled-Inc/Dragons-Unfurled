from random import randint

class Des():
    """
    Implémentation de la classe Des, un dés est définit par son nombre de face.
    En général, les faces de dés possibles sont : 4, 6, 8, 10, 12, 20, 100. 
    Par exemple, un dés comprenant 10 faces est numéroté de 1 à 10
    """
    def __init__(self, nb_face : int):
        self.__nb_face = nb_face

    def __str__(self):
        """
        Gère l'affichage d'un dé
        """
        modele = '\n'.join(['Le dé à {} faces.'])
        return modele.format(self.__nb_face)

    def lancer_un_des(self):
        return randint(1, self.__nb_face)

    @property
    def nb_face(self):
        return self.__nb_face

    @nb_face.setter
    def nb_face(self, value):
        self.__nb_face = value