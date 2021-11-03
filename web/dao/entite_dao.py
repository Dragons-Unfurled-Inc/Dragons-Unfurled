from objets_metier.entite import Entite 
from objets_metier.monstre import Monstre 
import requests as req
from abc import abstractstaticmethod

#le code est pas ouf mais vous avez une idée de comment faire, par contre c'est ptet plus à sa place dans le package web
class EntiteDAO:
    # @staticmethod
    # def creation_monstre(nom): 
    #     r = req.get('https://www.dnd5eapi.co/api/monsters/aboleth') 
    #     d=r.json()
    #     return(Monstre(nom,d["size"],d["alignment"],d['armor_class'],d['hit_points'],d['hit_dice'],d['speed'],d['strength'],d['dexterity'],d['constitution'],d['intelligence'],d['wisdom'],d['charisma'],d['proficiencies'],d['languages'],d['xp'])) 

    @staticmethod
    def diminution_pv(nom_entite: str): # Cette fonction n'est appelée que si l'entité a suffisamment de points de vies.
        return 

    @staticmethod
    def tuer(nom_entite: str): # Cette fonction réduit les points de vies des entités à 0.
        return 
