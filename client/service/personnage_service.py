from objets_metier.personnage import Personnage 
from utils.singleton import Singleton
import requests as req
'''
Experience Points	Level	Proficiency Bonus
0       1	+2
300  	2	+2
900	    3	+2
2.700	4	+2
6.500	5	+3
14.000	6	+3
23.000	7	+3
34.000	8	+3
48.000	9	+4
64.000	10	+4
85.000	11	+4
100.000	12	+4
120.000	13	+5
140.000	14	+5
165.000	15	+5
195.000	16	+5
225.000	17	+6
265.000	18	+6
305.000	19	+6
355.000	20	+6 '''
points = [0,300,900,2.700,6.500,14.000,23.000,34.000,48.000	,64.000	,85.000	,100.000,120.000,140.000,165.000,195.000,225.000, 265.000,305.000, 355.000]	
#Ceci est à stocker dans notre API ! 

class PersonnageService(metaclass=Singleton): 
    
    @staticmethod #après avoir posté ces données sur l'API on peut vérifier si avec un tel pt d'expérience un perso peut monter de niveau (ici version test)
    def montee_niveau(personnage: Personnage) -> None:
        i = 0
        while personnage.__caracteristiques_entite.experience > points[i]: 
            i += 1 
            personnage.__caracteristiques_entite.niveau = i+1 

    @staticmethod
    def liste_classe():
        r = req.get('https://www.dnd5eapi.co/api/classes')
        dicclasses = r.json()
        return [dicclasses['results'][i]['name'] for i in range(dicclasses['count'])]
    
    @staticmethod           
    def liste_race():
        r = req.get('https://www.dnd5eapi.co/api/races') 
        dicraces = r.json()
        return [dicraces['results'][i]['name'] for i in range(dicraces['count'])]
    

        