from objets_metier.entite import Entite 
from objets_metier.monstre import Monstre 
import requests as req 
from abc import abstractstaticmethod

#le code est pas ouf mais vous avez une idée de comment faire, par contre c'est ptet plus à sa place dans le package web
def rien(): 
    print("rien")
    
class CreationMonstre:
    @staticmethod
    def CreaMonstre(nom): 
        r = req.get('https://www.dnd5eapi.co/api/monsters/aboleth') 
        d=r.json()
        return(Monstre(nom,d["size"],d["alignment"],d['armor_class'],d['hit_points'],d['hit_dice'],d['speed'],d['strength'],d['dexterity'],d['constitution'],d['intelligence'],d['wisdom'],d['charisma'],d['proficiencies'],d['languages'],d['xp'])) 