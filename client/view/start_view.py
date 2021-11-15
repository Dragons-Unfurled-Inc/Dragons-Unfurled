from os import access
from PyInquirer import Separator, prompt
from client.view.abstract_view import AbstractView
from client.view.accueil_jeu_view import AccueilJeuView
from client.view.session import Session
from web.dao.utilisateur_dao import UtilisateurDAO
from client.view.creation_compte_view import CreaCompteView


class StartView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': ' Bonjour ! ',
                'choices': [
                    'S\'authentifier' ,
                    'Créer un compte' , 
                    'Quitter l\'application',
                    'La réponse D'

                ]
            }
        ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_connexion.txt', 'r', encoding="utf-8") as affichage2, open('client/dessins_ascii/texte/titre1.txt', 'r', encoding="utf-8") as affichage3, open('client/dessins_ascii/texte/titre2.txt', 'r', encoding="utf-8") as affichage4:
            print(affichage3.read(), affichage4.read(), affichage1.read(), affichage2.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'S\'authentifier':
            from client.view.connexion_view import ConnCompteView
            return ConnCompteView()
            from client.service.utilisateur_service import UtilisateurService
            utilisateur = UtilisateurService.connexion()
            if utilisateur.est_administrateur:
                from client.view.accueil_administrateur_view import AccueilAdministrateurView
                return AccueilAdministrateurView(utilisateur)
            else:
                from client.view.accueil_jeu_view import AccueilJeuView
                return AccueilJeuView(utilisateur)

        if reponse['choix'] == 'Créer un compte':
            # from client.service.utilisateur_service import UtilisateurService
            # utilisateur = UtilisateurService.creation_compte("joueur")
            # from client.view.accueil_jeu_view import AccueilJeuView
            return CreaCompteView()  
        
        if reponse['choix'] == 'Quitter l\'application':
            with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/dragons/dragon3.txt', 'r', encoding="utf-8") as affichage2, open('client/dessins_ascii/texte/au_revoir.txt', 'r', encoding="utf-8") as affichage3:
                print(affichage1.read(), affichage2.read(), affichage3.read())
            import sys
            sys.exit()
            
        if reponse['choix'] == 'La réponse D':
            from objets_metier.utilisateur import Utilisateur
            from client.view.session import Session
            Session.utilisateur=Utilisateur(connecte = True,mot_de_passe = "bla",identifiant = "id",est_administrateur = True,feed_backs = True)
            from client.view.accueil_jeu_view import AccueilJeuView
            return AccueilJeuView()   
        