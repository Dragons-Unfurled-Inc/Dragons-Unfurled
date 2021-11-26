from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session.
        """
        
        self.utilisateur = Utilisateur
        self.id_campagne = -1  # Les deux sauvegardes mémoire suivantes, permettent une simplification considérable de notre code lorsque nous passons d'un écran à un autre.
        self.id_donjon = -1  # Lors de leurs utilisations, nous vérifions qu'aucun droit n'est accordé par erreur.

        