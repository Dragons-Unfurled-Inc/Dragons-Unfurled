from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from client.view.maitre_du_jeu_view import MenuMJ
from client.view.joueur_view import MenuJoueur
from objets_metier.utilisateur import Utilisateur

class AccueilJeuView(AbstractView):

    def __init__(self, utilisateur:Utilisateur):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'{Session().identifiant} que souhaitez-vous faire ? ',
                'choices': [
                    'Rejoindre une campagne',
                    Separator(),
                    'Créer un personnage',
                    'Créer une campagne',
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
        if reponse['choix'] == 'Créer un personnage':
            from client.view.creation_personnage_view import MenuPersonnage
            return MenuPersonnage()
        if reponse['choix'] == 'Rejoindre une campagne':
            from client.view.joueur_view import MenuJoueur
            return MenuJoueur()
        if reponse['choix'] == 'Créer une campagne':
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ()    
        if reponse['choix'] == 'Se déconnecter':
            from client.view.deconnexion_view import MenuDeconnexion
            return MenuDeconnexion()
