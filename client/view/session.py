from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton

class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session.
        """
        self.est_administrateur = True
        self.utilisateur = Utilisateur