from entite import Entite

class Monstre(Entite):
    def __init__(self,nom,taille,type, sous_type, alignement,armure, hit_points, hit_dice, vitesse, force, dextérité, constitution, intelligence, sagesse, charisme,compétences,vulnerabilites_degat, resistances_degat,immunites_degat,immunites_etats, perception, langages,niveau_difficulte, experience,capacites_speciales, actions,actions_legendaires):
        super().__init__(self,nom, taille, alignement, hit_points, hit_dice, vitesse, armure, vitesse, force, dextérité, constitution, intelligence, sagesse, charisme,compétences, langages, experience)
        
c=['index', 'name', 'size', 'type', 'subtype', 'alignment', 'armor_class', 'hit_points', 
          'hit_dice', 'speed', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 
          'charisma', 'proficiencies', 'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
          'condition_immunities', 'senses', 'languages', 'challenge_rating', 'xp', 'special_abilities', 'actions', 
          'legendary_actions', 'url']

'''ct_keys(['type', 'subtype',
'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 
'condition_immunities', 'senses', 'challenge_rating', 
'xp', 'special_abilities', 'actions', 'legendary_actions', 'url'])'''