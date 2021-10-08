from entite import Entite
import requests as req

r = req.get('https://www.dnd5eapi.co/api/races')
dicraces = r.json()
listraces = [dicraces['results'][i]['name'] for i in range(dicraces['count'])]

c = req.get('https://www.dnd5eapi.co/api/classes')
dicclasses = c.json()
listclasses = [dicclasses['results'][i]['name'] for i in range(dicclasses['count'])]

class ClasseInexistante(Exception): 
    pass

class RaceInexistante(Exception):
    pass

class Personnage(Entite):
    def __init__(self,nom,taille,classe,race,niveau,alignement, hit_points, hit_dice, armure,vitesse, force, dextérité, constitution, intelligence, sagesse, charisme,compétences,abilités,traits,langages,equipement,lore, experience):
        super().__init__(self,nom, taille, alignement, hit_points, hit_dice, armure, vitesse, force, dextérité, constitution, intelligence, sagesse, charisme,compétences, langages, experience)
        self.classe = classe
        self.race = race 
        print('Création de', nom, 'de classe', classe, 'et de race', race)
        '''utiliser le module logging'''
        
        if classe not in listclasses:
            raise ClasseInexistante
        if race not in listraces :
            raise RaceInexistante
    def __del__(self):
        print('__del__', self.classe, self.race)

try:
    o=Personnage('Moi','Bard','Dwarf')
except ClasseInexistante:
    print('Cette classe est inexistante')
except RaceInexistante:
    print('Cette race est inexistante')
    
    
'''c=classe race niveau traits capac equipment lore 
Experience Points	Level	Proficiency Bonus
0   1	+2
300	2	+2
900	3	+2
2,700	4	+2
6,500	5	+3
14,000	6	+3
23,000	7	+3
34,000	8	+3
48,000	9	+4
64,000	10	+4
85,000	11	+4
100,000	12	+4
120,000	13	+5
140,000	14	+5
165,000	15	+5
195,000	16	+5
225,000	17	+6
265,000	18	+6
305,000	19	+6
355,000	20	+6'''