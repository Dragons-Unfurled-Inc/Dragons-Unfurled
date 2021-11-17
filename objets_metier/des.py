from random import randint
from pydantic import BaseModel

class Des(BaseModel):
    """
    Implémentation de la classe Des, un dés est définit par son nombre de face.
    En général, les faces de dés possibles sont : 4, 6, 8, 10, 12, 20, 100. 
    Par exemple, un dés comprenant 10 faces est numéroté de 1 à 10
    """
    nb_face : int
    valeur_des = int

    def lancer_le_des(self):
        self.valeur_des = randint(1, self.nb_face)

   