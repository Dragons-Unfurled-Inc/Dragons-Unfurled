from client.vue.abstract_vue import AbstractVue
from client.vue.accueil_jeu_vue import AccueilJeuVue
from client.vue.accueil_administrateur_vue import AccueilAdministrateurVue

from PyInquirer import prompt


class PassageAdminVue(AbstractVue):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': ' Que préférez-vous ? ',
                'choices': [
                    'Se connecter en tant que joueur',
                    'Se connecter en tant qu\'administrateur'

                ]
            }
        ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1:
            print(affichage1.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'Se connecter en tant que joueur':
            return AccueilJeuVue()
            
        if reponse['choix'] == 'Se connecter en tant qu\'administrateur':
            return AccueilAdministrateurVue()