import random as rd

from objets_metier.entite import Entite
from utils.singleton import Singleton


class Dommage(metaclass=Singleton): 
    """
    Cette classe permet de gérer automatiquement les dégats, suite à l'attaque d'une entité par une autre.
    """
    @staticmethod
    def frappe(type_attaque: str, attaquant: Entite, cible: Entite, bonus: int = 0) -> None: # Le type d'attaque est "force", "charisme", "intelligence" ou "dexterite".
        frappe_armure = rd.randint(1,20) # Ceci va determiner si l'attaque est bloqué par l'armure de l'ennemi.
        if frappe_armure > cible.caracteristiques_entite.classe_armure:
            degats = attaquant.caracteristiques_entite.type_attaque // 2 - 5 # On calcul la puissance d'attaque suivant le type d'attaque et les caractéristiques de l'attaquant.
            jet_critique = int(frappe_armure == 20) # Le dés de dégats est 2 fois plus gros dans le cas d'un jet critique
            diminution_pv = rd.randint(1,20*(1+jet_critique)) + degats + bonus # Bonus permet de prendre en compte l'arme ou le sort utilisé.
            cible.caracteristiques_entite.vie -= diminution_pv