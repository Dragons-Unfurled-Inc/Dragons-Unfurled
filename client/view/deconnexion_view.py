from PyInquirer import Separator, prompt, Validator, ValidationError

from client.view.abstract_view import AbstractView
from objets_metier.utilisateur import Utilisateur


class Deconnexion(AbstractView):
    #def

    def __init__(self, utilisateur:Utilisateur):
        self.__questions = [

    {
        'type': 'input',
        'name': 'confirmer_deco',
        'message': 'Confirmer la déconnexion.',

    },
    {
        'type': 'password',
        'name': 'Annuler',
        'message': 'Annuler.'
    }
    ]
        self.__utilisateur = utilisateur

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_deconnexion.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Confirmer la déconnexion':
            from client.view.start_view import StartView
            return StartView()
        if reponse['choix'] == 'Annuler':
            if self.__utilisateur.est_administrateur:
                from client.view.accueil_administrateur_view import AccueilAdministrateurView
                return AccueilAdministrateurView(self.__utilisateur)
            else:
                from client.view.accueil_jeu_view import AccueilJeuView
                return AccueilJeuView(self.__utilisateur)
            
            