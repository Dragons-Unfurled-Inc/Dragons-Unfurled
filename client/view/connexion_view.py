from client.service.utilisateur_service import UtilisateurService
from client.view.abstract_view import AbstractView
from PyInquirer import Separator, prompt
from PyInquirer import Validator, ValidationError
#from client.view.accueil_jeu_view import AccueilJeuView
from objets_metier.utilisateur import Utilisateur

class ConnCompteView(AbstractView):
    @staticmethod
    def __init__(self,precedent = "",tentative_num = 1):
        self.precedent = precedent
        self.tentative_num = tentative_num
        self.questions = [
                {
                    'type': 'input',
                    'name': 'Nom',
                    'message': 'Entrez votre nom de compte :',
                    'default' : self.precedent 
                },
                {
                    'type': 'password',
                    'name': 'mdp',
                    'message': 'Entrez votre mot de passe :'
                }
            ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        R = UtilisateurService.connexion(reponse['Nom'],reponse['mdp'])
        print(R)
        if not R : 
            if self.tentative_num < 2 : 
                print("Veuillez reessayer")
                return ConnCompteView(reponse['Nom'],self.tentative_num+1)
            print("Vous avez fait le nombre d'essais maximal. \n Vous allez être déconnecté.")
            import sys
            sys.exit()
