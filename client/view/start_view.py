from PyInquirer import Separator, prompt

from app.client.view.abstract_view import AbstractView
from app.client.view.session import Session




class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {Session().user_name}',
                'choices': [
                    'Creer un compte',
                    'S\'authentifier',
                    'Fin'

                ]
            }
        ]

    def display_info(self):
        with open('app/client/graphical_assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Creer un compte':
            from view.sign_in_example import SignInExample
            return SignInExample()
        if reponse['choix'] == 'Se connecter':
            from view.sign_in_example import SignInExample
            return SignInExample()
        if reponse['choix'] == 'Next':
            pass


