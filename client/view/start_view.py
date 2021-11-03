from os import access
from PyInquirer import Separator, prompt
from client.view.abstract_view import AbstractView
from client.view.accueil_jeu_view import AccueilJeuView
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
            from client.service.utilisateur_service import UtilisateurService
            utilisateur = UtilisateurService.connexion()
            if utilisateur.est_administrateur:
                from client.view.accueil_administrateur_view import AccueilAdministrateurView
                return AccueilAdministrateurView(utilisateur)
            else:
                from client.view.accueil_jeu_view import AccueilJeuView
                return AccueilJeuView(utilisateur)

        if reponse['choix'] == 'Créer un compte':
            from client.service.utilisateur_service import UtilisateurService
            utilisateur = UtilisateurService.creation_compte("joueur")
            from client.view.accueil_jeu_view import AccueilJeuView
            return AccueilJeuView(utilisateur)   
