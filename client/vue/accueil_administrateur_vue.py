from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from client.vue.start_vue import StartVue
from client.service.administrateur_service import AdministrateurService

from PyInquirer import Separator, prompt


class AccueilAdministrateurVue(AbstractVue):

    def __init__(self):
        utilisateur = Session.utilisateur
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'{utilisateur.identifiant} que souhaitez-vous faire ? ',
                'choices': [
                    'Consulter les feed-backs',
                    'Répondre à un feed-back',
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
        if reponse['choix'] == 'Consulter les feed-backs':
            AdministrateurService.consulter_feed_back_admin()
            return AccueilAdministrateurVue()

        if reponse['choix'] == 'Répondre à un feed-back':
            AdministrateurService.repondre_feed_back(input("Quel est le nom du joueur auquel vous voulez répondre ?\n"), input("Quelle est votre réponse ?\n"))
            return AccueilAdministrateurVue()
        
        if reponse['choix'] == 'Bannir un joueur': # Un administrateur ne peut pas être banni.
            AdministrateurService.bannir(input("Quel est le nom du joueur que vous souhaitez bannir ?\n"))
            return AccueilAdministrateurVue()

        if reponse['choix'] == 'Transférer ses droits': # Nous avons mis des controles pour que le nombre d'administrateur reste inchangé.
            AdministrateurService.transferer_droits_admin(input("Quel est le nom du joueur à qui vous voulez transférer vos droits ?\n"), utilisateur.identifiant)
            return StartVue()
        
        if reponse['choix'] == 'Se déconnecter':
            from client.vue.deconnexion_vue import Deconnexion
            return Deconnexion()