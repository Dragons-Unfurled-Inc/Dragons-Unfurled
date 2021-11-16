from client.service.utilisateur_service import UtilisateurService
from client.view.abstract_view import AbstractView
from PyInquirer import Separator, prompt
from PyInquirer import Validator, ValidationError
from client.view.accueil_jeu_view import AccueilJeuView

class CreaCompteView(AbstractView):
    def __init__(self,precedent = ""):
        self.precedent = precedent
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
                },
                {
                    'type': 'password',
                    'name': 'mdp2',
                    'message': 'Confirmez votre mot de passe :'
                }
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.questions)
        if not UtilisateurService.validation_creation_compte(reponse['Nom'],reponse['mdp'],reponse['mdp2']) : 
            return CreaCompteView(reponse['Nom'])
        UtilisateurService.creation_compte(reponse['Nom'],reponse['mdp'])
        return AccueilJeuView() 
            