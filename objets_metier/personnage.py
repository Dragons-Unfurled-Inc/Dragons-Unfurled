from typing import List, Optional

from pydantic import BaseModel

from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
from objets_metier.objet import Objet


class Personnage(Entite):
    classe: str
    race: str
    lore: str
    id_joueur: str 
    id_entite: str
    nom_entite: str
    caracteristiques_entite: Caracteristique        
    objets: Optional [List[Objet]] = []
    
    def __init__(self, classe : str, race : str, lore : str,id_joueur : str,id_entite : str,nom_entite : str, caracteristiques_entite: Caracteristique, objets: Optional [List[Objet]] = []) :  
        super().__init__( classe = classe, race = race,lore = lore, id_joueur= id_joueur,id_entite = id_entite,nom_entite = nom_entite,caracteristiques_entite = caracteristiques_entite,objets = objets)
        
    class Config:
        schema_extra = {
            "example": {
                "classe": "Barbare",
                "race": "Nain",
                "lore": "Un nain très barbu qui vient d/'une mine",
                "id_joueur": -1,
                "id_entite": -1,
                "nom_entite": "Martin",
                "caracteristiques_entite": {
                        "nom_entite":"Nom", 
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
        Affichage d'un personnage
        """
        aff_obj = '            Vide'
        if self.objets != None :
            aff_obj = ''
            curs = len(self.objets)
            for obj in self.objets: 
                if curs == 1:
                    aff_obj += Objet.__str__(obj)
                else : 
                    aff_obj += Objet.__str__(obj) + '\n \n'
                    curs -= 1 
        modele = '\n'.join(['        Classe : {} \n        Race : {} \n        Lore : {}\n        Identifiant joueur : {} \n        Identifiant personnage : {} \n        Nom personnage : {} \n        Caractéristiques : \n{} \n        Objets : \n{}\n'])
        return modele.format(self.classe,
                             self.race,
                             self.lore,
                             self.id_joueur,
                             self.id_entite,
                             self.nom_entite,
                             Caracteristique.str(self.caracteristiques_entite),
                             aff_obj) 

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
