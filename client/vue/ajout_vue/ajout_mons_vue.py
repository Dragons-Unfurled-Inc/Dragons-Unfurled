from PyInquirer import prompt
from client.service.monstre_service import MonstreService
from client.vue.abstract_vue import AbstractVue
from objets_metier.entite import Entite
from web.dao.entite_dao import EntiteDAO

class AjoutMonsVue(AbstractVue):
    
    @staticmethod
    def choix(reponse): 
        return MonstreService.ImportMonstreParType(reponse['type'])
    
    def __init__(self):
        #self.joueur = joueur 
        self.liste_types = MonstreService.ImportListeTypes()
        self.questions = [
            {
                'type': 'list',
                'name': 'type',
                'message': 'Choisissez le type de monstre que vous voulez importer :',
                'choices': self.liste_types
            },
            {
                'type': 'list',
                'name': 'monstre',
                'message': f'Choisissez le monstre que vous voulez importer :',
                'choices': AjoutMonsVue.choix,
            }
        ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        monstre = MonstreService.ImportMonstreWeb(reponse['monstre'])
        EntiteDAO.ajoute_entite(monstre)
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ()