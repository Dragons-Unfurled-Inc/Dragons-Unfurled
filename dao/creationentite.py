from objets_metier.entite import Entite 
from objets_metier.monstre import Monstre 
import requests as req 
from abc import abstractstaticmethod
class CreationMonstre:
    @staticmethod
    def CreaMonstre(nom):
        r = req.get('https://www.dnd5eapi.co/api/monsters/aboleth')
        d=r.json()
        print(d.keys())
        print(d.keys())
        return(Monstre(nom,d["size"],d["alignment"],d['armor_class'],d['hit_points'],d['hit_dice'],d['speed'],d['strength'],d['dexterity'],d['constitution'],d['intelligence'],d['wisdom'],d['charisma'],d['proficiencies'],d['languages'],d['xp']))