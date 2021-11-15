from PyInquirer import Separator, prompt, Validator, ValidationError

from client.view.abstract_view import AbstractView
from objets_metier.utilisateur import Utilisateur
from client.view.session import Session
from client.view.accueil_jeu_view import AccueilJeuView
from client.view.passage_admin_view import PassageAdminView
from client.service.utilisateur_service import UtilisateurService


class Deconnexion(AbstractView):

    def __init__(self, utilisateur:Utilisateur):
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
            from client.view.start_view import StartView
            return StartView()
        if reponse['choix'] == 'Annuler':
            est_administrateur = UtilisateurService.est_admin(utilisateur.nom_utilisateur)
            if est_administrateur:
                return PassageAdminView(utilisateur)
            return AccueilJeuView(utilisateur)
            