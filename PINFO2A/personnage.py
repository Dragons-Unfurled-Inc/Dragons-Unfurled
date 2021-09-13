r = req.get('https://www.dnd5eapi.co/api/races')
dicraces = r.json()
listraces = [dicraces['results'][i]['name'] for i in range(d['count'])]

c = req.get('https://www.dnd5eapi.co/api/classes')
dicclasses = c.json()
listclasses = [dicclasses['results'][i]['name'] for i in range(d['count'])]

class ClasseInexistante(Exception): 
    pass

class RaceInexistante(Exception):
    pass

class Personnage:
    def __init__(self,nom,classe,race) -> None:    
        self.nom = nom
        self.classe = classe
        self.race = race 
        print('Création de', nom, 'de classe', classe, 'et de race', race)
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
    
    
c='classe race niveau stats capac equipment nom language lore'