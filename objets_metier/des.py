from random import randint
from pydantic import BaseModel

class Des(BaseModel):
    """
    Implémentation de la classe Des, un dés est définit par son nombre de face.
    En général, les faces de dés possibles sont : 4, 6, 8, 10, 12, 20, 100. 
    Par exemple, un dés comprenant 10 faces est numéroté de 1 à 10
    """
    _nb_face : int
    _valeur_des = None 

    class Config:
        underscore_attrs_are_private = True

    def lancer_le_des(self):
        self._valeur_des = randint(1, self._nb_face)

    @property
    def nb_face(self):
        return self._nb_face

    @nb_face.setter
    def nb_face(self, value):
        self._nb_face = value

    @property
    def valeur_des(self):
        return self._valeur_des
 
    @valeur_des.setter
    def valeur_des(self, value):
        self._valeur_des = value 