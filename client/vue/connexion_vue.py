from client.service.utilisateur_service import UtilisateurService
from client.vue.abstract_vue import AbstractVue
from client.vue.accueil_jeu_vue import AccueilJeuVue
from client.vue.passage_admin_vue import PassageAdminVue

from PyInquirer import prompt


class ConnCompteVue(AbstractVue):
    
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
        if not UtilisateurService.connexion(reponse['Nom'],reponse['mdp']): 
            if self.tentative_num < 2 : 
                print("Veuillez reessayer")
                return ConnCompteVue(reponse['Nom'],self.tentative_num+1)
            print("Vous avez fait le nombre d'essais maximal. \n Vous allez être déconnecté.")
            import sys
            sys.exit()
        if UtilisateurService.est_admin(reponse['Nom']):
            return PassageAdminVue()
        return AccueilJeuVue()