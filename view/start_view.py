from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session




class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {Session().user_name}',
                'choices': [
                    'Rejoindre une campagne',
                    'Créer un personnage',
                    'Se déconnecter',
                    
                ]
            }
        ]

    def display_info(self):
        with open('graphical_assets/dragon.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Créer un personnage':
            from view.test import MenuPersonnage
            return MenuPersonnage()
        else :
            pass 

