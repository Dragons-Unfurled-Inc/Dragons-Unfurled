from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from client.vue.accueil_jeu_vue import AccueilJeuVue
from client.vue.passage_admin_vue import PassageAdminVue
from client.service.utilisateur_service import UtilisateurService

from PyInquirer import prompt

class Deconnexion(AbstractVue):

    def __init__(self):
        utilisateur = Session.utilisateur
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'{utilisateur.identifiant} que souhaitez-vous faire ? ',
                'choices': [
                    'Confirmer la déconnexion',
                    'Annuler'
                    
                ]
            }
        ]
        self.__utilisateur = utilisateur

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_deconnexion.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        utilisateur = Session.utilisateur
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Confirmer la déconnexion':
            from client.vue.start_vue import StartVue
            return StartVue()
        if reponse['choix'] == 'Annuler':
            est_administrateur = UtilisateurService.est_admin(utilisateur.identifiant)
            if est_administrateur:
                return PassageAdminVue()
            return AccueilJeuVue()
            