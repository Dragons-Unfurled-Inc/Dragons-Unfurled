from PyInquirer import Separator, prompt
from client.view import accueil_jeu_view


from client.view.abstract_view import AbstractView
from web.dao.jet_dao import JetDAO
from client.view.session import Session
from objets_metier.joueur import Joueur


class MenuJoueur(AbstractView):

    def __init__(self, joueur, campagne):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Modifier la fiche de votre personnage',
                    Separator(),
                    'Consulter la fiche de votre personnage',
                    Separator(),
                    'Lancer des dés',
                    Separator(),
                    'Consulter les résultats des jets',
                    Separator(),
                    'Donner un feedback',
                    Separator(),
                    'Quitter la campagne',
                    
                ]
            }
        ]
        self.joueur = joueur
        self.campagne = campagne

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_joueur.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Modifier la fiche de votre personnage':
            Joueur.modifier_personnage(self.joueur,self.campagne)
            from client.view.joueur_view import MenuJoueur
            return MenuJoueur(self.joueur,self.campagne)
            
        if reponse['choix'] == 'Consulter la fiche de votre personnage':
            Joueur.consulter_personnage(self.joueur,self.campagne)
            from client.view.joueur_view import MenuJoueur
            
        if reponse['choix'] == 'Lancer des dés':
            from client.view.des_view import MenuDes
            return MenuDes(self.joueur, self.campagne)   



        if reponse['choix'] == 'Consulter les résultats des jets':
            JetDAO.consulter_tous_les_jets(self.campagne,self.joueur)
            from client.view.joueur_view import MenuJoueur
            return MenuJoueur(self.joueur,self.campagne)


        if reponse['choix'] == 'Donner un feedback':
            message = input("Quel est le feedback que vous souhaitez poster ?")
            Joueur.donner_feed_back(self.joueur,message)
            return MenuJoueur(self.joueur,self.campagne)

        if reponse['choix'] == 'Quitter la campagne':
            from client.view.accueil_jeu_view import AccueilJeuView
            return AccueilJeuView(self.joueur)
        
