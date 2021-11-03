from typing import List, Optional

from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.entite import Entite

class Personnage(Entite):

    def __init__(self, classe: str,
                       race: str,
                       lore: str,
                       id_joueur: str, 
                       id_entite: str,
                       nom_entite: str,                  
                       caracteristiques_entite: Caracteristique,
                       objets: Optional[List[Objet]] = None ) -> None: 

        super().__init__(
            id_joueur= id_joueur,
            id_entite = id_entite,
            caracteristiques_entite = caracteristiques_entite,
            objets = objets
            ) 
        self.__classe = classe
        self.__race = race
        self.__lore = lore
        self.__nom_entite = nom_entite

    def __str__(self): 
        """
        Affichage d'un personnage
        """
        aff_obj = '    Vide'
        if self.objets != None :
            aff_obj = ''
            for obj in self._objets: 
                aff_obj += Objet.__str__(obj)
                aff_obj += '\n'
        modele = '\n'.join(['Classe : {} \nRace : {} \nLore : {}\nIdentifiant joueur : {} \nIdentifiant personnage : {} \nNom personnage : {} \nCaractéristiques : \n{} \nObjets : \n{}\n'])
        return modele.format(self.__classe,
                             self.__race,
                             self.__lore,
                             self._id_joueur,
                             self._id_entite,
                             self.__nom_entite,
                             Caracteristique.__str__(self._caracteristiques_entite),
                             'Vide') 


    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, value):
        self.__classe = value 

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        self.__race = value 

    @property
    def lore(self):
        return self.__lore

    @lore.setter
    def lore(self, value):
        self.__lore = value         

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