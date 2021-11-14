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
        R = UtilisateurService.validation_creation_compte(reponse['Nom'],reponse['mdp'],reponse['mdp2'])
        #plus tard, R sera juste le booleen de validation de compte et le compte sera stocké en session
        #pour l'instant, c'est la liste qui contient l'utilisateur qui est entré sur cet ecran et le booleen qui indique si il est valide
        if not R[1] : 
            return CreaCompteView(reponse['Nom'])
        if R[1]:
            utilisateur = UtilisateurService.creation_compte(R[0],'joueur')
            return AccueilJeuView(utilisateur) 
            