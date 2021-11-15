from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from objets_metier.utilisateur import Utilisateur
from client.service.administrateur_service import AdministrateurService

class AccueilAdministrateurView(AbstractView):

    def __init__(self):
        utilisateur = Session.utilisateur
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'{utilisateur.identifiant} que souhaitez-vous faire ? ',
                'choices': [
                    'Consulter les feedbacks',
                    'Bannir un joueur',
                    'Transférer ses droits',
                    Separator(),
                    'Se déconnecter',
                    
                ]
            }
        ] 

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_administrateur.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        utilisateur = Session.utilisateur
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Consulter les feedbacks':
            AdministrateurService.consulter_feed_back_admin()
            return AccueilAdministrateurView()
        
        if reponse['choix'] == 'Bannir un joueur':
            AdministrateurService.bannir(input("Quel est le nom du joueur que vous souhaitez bannir ?"))
            return AccueilAdministrateurView()

        if reponse['choix'] == 'Transférer ses droits':
            AdministrateurService.transferer_droits_admin(input("Quel est le nom du joueur à qui vous voulez transférer vos droits ?"), utilisateur.identifiant)
            return AccueilAdministrateurView()
        
        if reponse['choix'] == 'Se déconnecter':
            from client.view.deconnexion_view import Deconnexion
            return Deconnexion()