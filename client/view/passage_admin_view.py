from client.view.abstract_view import AbstractView
from PyInquirer import Separator, prompt
from PyInquirer import Validator, ValidationError
from client.view.session import Session
from client.view.accueil_jeu_view import AccueilJeuView
from client.view.accueil_administrateur_view import AccueilAdministrateurView
from objets_metier.utilisateur import Utilisateur

class PassageAdminView(AbstractView):

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
            return AccueilJeuView()
            
        if reponse['choix'] == 'Se connecter en tant qu\'administrateur':
            return AccueilAdministrateurView()