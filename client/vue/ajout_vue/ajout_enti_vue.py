from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session

from PyInquirer import prompt



class AjoutEntiVue(AbstractVue):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez vous ajouter :',
                'choices': [
                    'Le personnage d\'un joueur' ,
                    'Un monstre' , 
                    'Un personnage non joueur (PNJ)'
                ]
            }
        ]
        self.joueur = Session.utilisateur 
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'Le personnage d\'un joueur':
            from client.vue.ajout_vue.ajout_pers_vue import AjoutPersVue
            return AjoutPersVue()
        
        if reponse['choix'] == 'Un monstre' :
            from client.vue.ajout_vue.ajout_mons_vue import AjoutMonsVue
            return AjoutMonsVue()
        
        if reponse['choix'] == 'Un personnage non joueur (PNJ)' :
            from client.vue.ajout_vue.ajout_pnj_vue import AjoutPNJVue
            return AjoutPNJVue()
        