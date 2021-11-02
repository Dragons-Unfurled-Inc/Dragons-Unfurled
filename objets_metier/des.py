from random import randint

class Des():
    """
    Implémentation de la classe Des, un dés est définit par son nombre de face.
    En général, les faces de dés possibles sont : 4, 6, 8, 10, 12, 20, 100. 
    Par exemple, un dés comprenant 10 faces est numéroté de 1 à 10
    """
    def __init__(self, nb_face : int):
        self.__nb_face = nb_face

    def lancer_un_des(self):
        return randint(1, self.__nb_face)

