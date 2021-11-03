from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from objets_metier.utilisateur import Utilisateur
from client.service.administrateur_service import AdministrateurService

class AccueilAdministrateurView(AbstractView):

    def __init__(self, utilisateur:Utilisateur):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'{Session().identifiant} que souhaitez-vous faire ? ',
                'choices': [
                    'Consulter les feedbacks',
                    'Bannir un joueur',
                    Separator(),
                    'Se déconnecter',
                    
                ]
            }
        ]
        self.utilisateur = utilisateur    

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Consulter les feedbacks':
            AdministrateurService.consulter_feed_back_admin()
        if reponse['choix'] == 'Bannir un joueur':
            AdministrateurService.bannir(input("Quel identifiant-utilisateur souhaitez-vous bannir ?"))
        if reponse['choix'] == 'Se déconnecter':
            import sys
            sys.exit()