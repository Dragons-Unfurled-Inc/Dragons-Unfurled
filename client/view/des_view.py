from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session

class MenuDes(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Attaquer une entité',
                    Separator(),
                    'Lancer librement des dés',
                    Separator(),
                    'Changer le mode de révélation des dés',
                    Separator(),
                    'Quitter le menu de lancer de dés',
                ]
            }
        ]
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Attaquer une entité':
            pass
        if reponse['choix'] == 'Lancer librement des dés':
            pass
        if reponse['choix'] == 'Changer le mode de révélation des dés':
            pass 
        if reponse['choix'] == 'Quitter le menu de lancer de dés':
            pass 