from typing import List

from utils.singleton import Singleton
from objets_metier.feedback import Feedback
from objets_metier.utilisateur import Utilisateur

class AdministrateurService(metaclass=Singleton):

    def bannir(self, id_utilisateur:str):
        None
    
    def consulter_feed_back_admin(self):
        None