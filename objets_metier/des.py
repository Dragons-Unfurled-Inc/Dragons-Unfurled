from random import randint

class Des():
    """
    
    """
    def __init__(self, nb_face : int):
        self.__nb_face = nb_face

    def lancer_un_des(self):
        return randint(1, self.__nb_face)

