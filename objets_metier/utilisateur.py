from typing import List
from pydantic import BaseModel

from objets_metier.feedback import Feedback

class Utilisateur(BaseModel):
    _connecte : bool
    _mot_de_passe : str
    _identifiant : str
    _est_administrateur : bool
    _feed_backs : List[Feedback] = []

    class Config:
        underscore_attrs_are_private = True

    def se_connecter(self, id : str, mdp : str):
        None
    
    def creer_compte(self, id : str, mdp : str):
        None
    
    def se_deconnecter(self):
        None 

    def donner_feed_back(self, message : str):
        None
    
    def consulter_feed_back(self):
        None

    @property
    def connecte(self):
        return self._connecte
    
    @connecte.setter
    def connecte(self, value):
        self._connecte = value

    @property
    def mot_de_passe(self):
        return self._mot_de_passe
    
    @mot_de_passe.setter
    def mot_de_passe(self, value):
        self._resultat = value

    @property
    def identifiant(self):
        return self._identifiant
    
    @identifiant.setter
    def identifiant(self, value):
        self._identifiant = value

    @property
    def est_administrateur(self):
        return self._est_administrateur
    
    @est_administrateur.setter
    def est_administrateur(self, value):
        self._est_administrateur = value

    @property
    def feed_backs(self):
        return self._feed_back
    
    @feed_backs.setter
    def feed_back(self, value):
        self._feed_back = value