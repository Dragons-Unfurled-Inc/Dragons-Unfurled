import copy
from typing import List, Optional

from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from entite import Entite

class Monstre(Entite):
    
    def __init__(self, type: str,
                       id_joueur: str, 
                       id_entite: str,                  
                       caracteristiques_entite: Caracteristique,
                       objets: Optional[List[Objet]] = None ,
                        ) -> None: 

        Entite.__init__(self, id_joueur, id_entite, caracteristiques_entite, objets)
        self.__type = type









c=['index', 'name', 'size', 'type', 'subtype', 'alignment', 'armor_class', 'hit_points', 
          'hit_dice', 'speed', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 
          'charisma', 'proficiencies', 'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
          'condition_immunities', 'senses', 'languages', 'challenge_rating', 'xp', 'special_abilities', 'actions', 
          'legendary_actions', 'url']

'''ct_keys(['type', 'subtype',
'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
'condition_immunities', 'senses', 'challenge_rating', 
'xp', 'special_abilities', 'actions', 'legendary_actions', 'url'])'''