from client.vue.session import Session
from client.vue.abstract_vue import AbstractVue

from web.service.jet_service import JetService

from objets_metier.utilisateur import Utilisateur
from objets_metier.joueur import Joueur

from PyInquirer import Separator, prompt



class MenuJoueur(AbstractVue):

    def __init__(self):
        self.joueur = Session.utilisateur
        self.id_campagne = Session.id_campagne
        
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session.utilisateur.identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Modifier la fiche de votre personnage',
                    'Consulter la fiche de votre personnage',
                    Separator(),
                    'Lancer des dés',
                    'Consulter les résultats des jets',
                    Separator(),
                    'Donner un feedback',
                    Separator(),
                    'Quitter la campagne',
                    
                ]
            }
        ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_joueur.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Modifier la fiche de votre personnage':
            from client.vue.modif_perso_vue import ModifCaracVue
            return ModifCaracVue()
            
        if reponse['choix'] == 'Consulter la fiche de votre personnage':
            Joueur.consulter_personnage(self.id_campagne, self.joueur.identifiant)
            from client.vue.joueur_vue import MenuJoueur
            return MenuJoueur()
            
        if reponse['choix'] == 'Lancer des dés':
            from client.vue.des_vue import MenuDes
            return MenuDes()   

        if reponse['choix'] == 'Consulter les résultats des jets':
            JetService.consulter_tous_les_jets(self.id_campagne)
            from client.vue.joueur_vue import MenuJoueur
            return MenuJoueur()


        if reponse['choix'] == 'Donner un feedback':
            message = input("Quel est le feedback que vous souhaitez poster ? \n")
            Utilisateur.ecrire_un_feed_back(message)
            from client.vue.joueur_vue import MenuJoueur
            return MenuJoueur()

        if reponse['choix'] == 'Quitter la campagne':
            from client.vue.accueil_jeu_vue import AccueilJeuVue
            return AccueilJeuVue()
        
