from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.monstre_service import MonstreService
from client.vue.abstract_vue import AbstractVue
from objets_metier.entite import Entite
from PyInquirer import Separator, Token, prompt, style_from_dict
from web.dao.entite_dao import EntiteDAO

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#f40099',  
    Token.Pointer: '#1f5100 bold',
    Token.Instruction: '#a2ff92 italic',  
    Token.Answer: '#f44336 bold',
    Token.Question: '#f7be00',
})

class AjoutMonsVue(AbstractVue):
    
    @staticmethod
    def choix(reponse): 
        return MonstreService.ImportMonstreParType(reponse['type'])
    
    def __init__(self):
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
        reponse = prompt(self.questions,style = style)
        monstre = MonstreService.ImportMonstreWeb(reponse['monstre'])
        id_entite = EntiteDAO.ajoute_entite(monstre)
        print(id_entite)
        MaitreDuJeuService.ajouter_entite_campagne(id_entite)  
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ()
    
    