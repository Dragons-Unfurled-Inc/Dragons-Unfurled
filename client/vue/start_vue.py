from PyInquirer import prompt
from client.vue.abstract_vue import AbstractVue
from objets_metier.joueur import Joueur
from client.vue.creation_compte_vue import CreaCompteVue


class StartVue(AbstractVue):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': ' Bonjour ! ',
                'choices': [
                    'S\'authentifier' ,
                    'Créer un compte' , 
                    'Importer une sauvegarde',
                    'Quitter l\'application'

                ]
            }
        ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_connexion.txt', 'r', encoding="utf-8") as affichage2, open('client/dessins_ascii/texte/titre1.txt', 'r', encoding="utf-8") as affichage3, open('client/dessins_ascii/texte/titre2.txt', 'r', encoding="utf-8") as affichage4:
            print(affichage3.read(), affichage4.read(), affichage1.read(), affichage2.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'S\'authentifier':
            from client.vue.connexion_vue import ConnCompteVue
            return ConnCompteVue()

        if reponse['choix'] == 'Créer un compte':
            return CreaCompteVue()  

        if reponse['choix'] == 'Importer une sauvegarde':
            print("La sauvegarde a été restaurée.")
            return StartVue() 
        
        if reponse['choix'] == 'Quitter l\'application':
            with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/dragons/dragon3.txt', 'r', encoding="utf-8") as affichage2, open('client/dessins_ascii/texte/au_revoir.txt', 'r', encoding="utf-8") as affichage3:
                print(affichage1.read(), affichage2.read(), affichage3.read())
            import sys
            sys.exit()
            
        if reponse['choix'] == 'La réponse D':
            from client.vue.session import Session
            Session.utilisateur=Joueur(identifiant = "id",id_campagne="61")
            from client.vue.accueil_jeu_vue import AccueilJeuVue
            return AccueilJeuVue()   
        