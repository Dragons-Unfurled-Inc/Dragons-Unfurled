from entite import Entite

class Personnage(Entite):
    def __init__(self, classe, race, lore, id_joueur, id_entite, nom_entite, caracteristiques_entite, objets):
        super().__init__(self, id_joueur, id_entite, nom_entite, caracteristiques_entite, objets)
        self.classe = classe
        self.race = race
        self.lore = lore
        print('Création de', nom_entite, 'de classe', classe, 'et de race', race)
        '''utiliser le module logging'''
    
    def __del__(self):
        print('__del__', self.classe, self.race)


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