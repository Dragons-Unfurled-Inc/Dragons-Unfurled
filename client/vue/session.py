from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session.
        """
        #self.est_administrateur = True
        self.utilisateur = Utilisateur
        self.id_campagne = -1

        @staticmethod
        def upgrade_util_jou():
            self.utilisateur
         
        @staticmethod
        def upgrade_id_campagne():
            self.id_campagne