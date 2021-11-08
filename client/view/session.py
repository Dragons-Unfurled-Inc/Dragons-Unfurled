from utils.singleton import Singleton

class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session.
        """
        self.connecte = False
        self.mot_de_passe: str = Testest
        self.identifiant: str = Julien
        self.est_administrateur = True