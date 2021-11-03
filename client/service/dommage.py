import random as rd

from objets_metier.entite import Entite


class Dommage : 
    """
    Cette classe permet de gérer automatiquement les dégats, suite à l'attaque d'une entité par une autre.
    """
    @staticmethod
    def frappe(type_attaque: str, attaquant: Entite, cible: Entite) -> str: # Le type d'attaque est "force", "charisme", "intelligence" ou "dexterite".
        if rd.randint(1,20) > cible.caracteristiques_entite
