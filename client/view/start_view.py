from PyInquirer import Separator, prompt
from client.view.abstract_view import AbstractView
from client.view.session import Session


class StartView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' Bonjour {Session().identifiant} ',
                'choices': [
                    'S\'authentifier' ,
                    'Créer un compte'

                ]
            }
        ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'S\'authentifier':
            from client.view.authentification_view import Authentification
            return Authentification()
