from client.service.recherche import Recherche

from objets_metier.entite import Entite

from utils.singleton import Singleton
import random as rd

class Dommage(metaclass=Singleton): 
    """
    Cette classe permet de gérer automatiquement les dégats, suite à l'attaque d'une entité par une autre.
    """
    @staticmethod
    def frappe(attaquant: Entite, cible: Entite, bonus: int = 0, type_attaque: str = "i") -> None: # Le type d'attaque est "force", "charisme", "intelligence" ou "dexterite".
        frappe_armure = rd.randint(1,20) # Ceci va determiner si l'attaque est bloquée par l'armure de l'ennemi.
        if frappe_armure > cible.caracteristiques_entite.classe_armure:
            degat = rd.randint(1,20)
            if type_attaque == "d":
                degats = degat + attaquant.caracteristiques_entite.dexterite // 2 - 5 # On calcule la puissance d'attaque suivant le type d'attaque et les caractéristiques de l'attaquant.
            if type_attaque == "i":
                degats = degat + attaquant.caracteristiques_entite.intelligence // 2 - 5 
            if type_attaque == "f":
                degats = degat + attaquant.caracteristiques_entite.force // 2 - 5 
            if type_attaque == "c":
                degats = degat + attaquant.caracteristiques_entite.charisme // 2 - 5 
            else:
                degats = degat + attaquant.caracteristiques_entite.force // 2 - 5
                print("Attention, une attaque de type force a été effectué par défault car le type entré était incorect.")
            jet_critique = int(frappe_armure == 20) # Le dés de dégats est 2 fois plus gros dans le cas d'un jet critique
            diminution_pv = rd.randint(1,20*(1+jet_critique)) + degats + bonus # Bonus permet de prendre en compte l'arme ou le sort utilisé.
            Recherche.modifie_pv(cible, diminution_pv)
            if cible.caracteristiques_entite.vie > diminution_pv:
                print("L'ennemi : ", cible.caracteristiques_entite.nom_entite, " est passé de ", cible.caracteristiques_entite.vie, " à ", cible.caracteristiques_entite.vie - diminution_pv, " points de vie.")
            else:
                print("L'ennemi : ", cible.caracteristiques_entite.nom_entite, " a été vaincu.\nSes points de vies sont à 0.")
        else:
            print("L'attaque a été contrée par l'armure de l'ennemi.")
