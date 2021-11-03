from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from client.view.mj import MenuMJ
from client.view.joueur import MenuJoueur

class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {Session().user_name}',
                'choices': [
                    'Rejoindre une campagne',
                    Separator(),
                    'Créer un personnage',
                    Separator(),
                    'Créer une campagne',
                    Separator(),
                    'Se déconnecter',
                    
                ]
            }
        ]

    def display_info(self):
        with open('dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Créer un personnage':
            from client.view.creation_pers import MenuPersonnage
            return MenuPersonnage()
        if reponse['choix'] == 'Rejoindre une campagne':
            from client.view.joueur import MenuJoueur
            return MenuJoueur()
        if reponse['choix'] == 'Créer une campagne':
            from client.view.mj import MenuMJ
            return MenuMJ()    
        if reponse['choix'] == 'Se déconnecter':
            pass
