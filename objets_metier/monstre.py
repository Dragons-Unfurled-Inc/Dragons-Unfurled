from typing import List, Optional
from pydantic import BaseModel
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.entite import Entite

class Monstre(Entite,BaseModel):
    
    id_joueur: str
    id_entite: str     
    type: str            
    caracteristiques_entite: Caracteristique
    objets: Optional[List[Objet]] = None
    
    def __init__(self,id_joueur : str,id_entite : str,type : str,caracteristiques_entite : Caracteristique):
        super().__init__(id_joueur = id_joueur,id_entite = id_entite,type = type,caracteristiques_entite = caracteristiques_entite)
    
    class Config:
        underscore_attrs_are_private = True
        schema_extra = {
            "example": {
                "type": "Gobelin",
                "id_joueur": 5,
                "id_entite":4,
                "caracteristiques_entite": { 
                        "attaques":["Attaques"], 
                        "capacites":["Capacité"], 
                        "languages":["langages"],
                        "description":"des"
                },
                "objets" : [{
                        "id_objet" : "4", 
                        "nom_objet" : "objet test",
                        "description" : "pioche"
                } ]
            }
        }

    def __str__(self):
        """
        Affichage des monstres 
        """
        aff_obj = '        Vide'
        if self.objets != None :
            curs = len(self.objets)
            aff_obj = ''
            for obj in self.objets: 
                if curs == 1 :
                    aff_obj += Objet.__str__(obj)
                else :
                    aff_obj += Objet.__str__(obj) + '\n \n'
                    curs -= 1
        modele = '\n'.join(['        Type : {} \n        Identifiant joueur : {} \n        Identifiant monstres : {} \n        Caractéristiques : \n{} \n        Objets : \n{}'])
        return modele.format(self.type,
                             self.id_joueur,
                             self.id_entite,
                             Caracteristique.__str__(self.caracteristiques_entite),
                             aff_obj)

    



c=['index', 'name', 'size', 'type', 'subtype', 'alignment', 'armor_class', 'hit_points', 
          'hit_dice', 'speed', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 
          'charisma', 'proficiencies', 'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
          'condition_immunities', 'senses', 'languages', 'challenge_rating', 'xp', 'special_abilities', 'actions', 
          'legendary_actions', 'url']

'''ct_keys(['type', 'subtype',
'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
'condition_immunities', 'senses', 'challenge_rating', 
'xp', 'special_abilities', 'actions', 'legendary_actions', 'url'])'''