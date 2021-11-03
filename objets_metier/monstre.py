from typing import List, Optional

from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.entite import Entite

class Monstre(Entite):
    
    def __init__(self, type: str,
                       id_joueur: str, 
                       id_entite: str,                  
                       caracteristiques_entite: Caracteristique,
                       objets: Optional[List[Objet]] = None ) -> None: 

        super().__init__(
            id_joueur= id_joueur,
            id_entite = id_entite,
            caracteristiques_entite = caracteristiques_entite,
            objets = objets,
            )

        self.__type = type
    
    def __str__(self):
        """
        Affichage des monstres 
        """
        modele = '\n'.join(['Type : {} \nIdentifiant joueur : {} \nIdentifiant monstres : {} \nCaractéristiques : {} \nObjets : {}'])
        aff_obj = ''
        for obj in self._objets: 
            aff_obj += print(obj)
            aff_obj += '\n'
        return modele.format(self.__type,
                             self._id_joueur,
                             self._id_entite,
                             print(self._caracteristiques_entite),
                             aff_obj)


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value






c=['index', 'name', 'size', 'type', 'subtype', 'alignment', 'armor_class', 'hit_points', 
          'hit_dice', 'speed', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 
          'charisma', 'proficiencies', 'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
          'condition_immunities', 'senses', 'languages', 'challenge_rating', 'xp', 'special_abilities', 'actions', 
          'legendary_actions', 'url']

'''ct_keys(['type', 'subtype',
'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
'condition_immunities', 'senses', 'challenge_rating', 
'xp', 'special_abilities', 'actions', 'legendary_actions', 'url'])'''