from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from objets_metier.joueur import Joueur
from client.view.session import Session
from web.dao.jet_dao import JetDAO
class MenuMJ(AbstractView):

    def __init__(self, joueur, campagne):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Ajouter ou supprimer une entité',
                    Separator(),
                    'Créer un donjon',
                    Separator(),
                    'Réaliser une action sur un donjon',
                    Separator(),
                    'Créer une entité',
                    Separator(),
                    'Consulter la fiche d\'une entité',
                    Separator(),
                    'Modifier la fiche d\'une entité',
                    Separator(),
                    'Lancer des dés',
                    Separator(),
                    'Consulter les jets',
                    Separator(),
                    'Donner un feedback',
                    Separator(),
                    'Sauvegarder l\état de la campagne',
                    Separator(),
                    'Quitter la campagne',
                    
                ]
            }
        ]
        self.joueur = joueur
        self.campagne = campagne
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Ajouter ou supprimer une entité':
            message = input("Voulez-vous ajouter une entité à votre campagne ? \n Faîtes entrer si oui et écrivez quelque-chose sinon.")
            if message:
                print("Voici la liste des entités:")
                

        if reponse['choix'] == 'Créer un donjon':
            pass
        if reponse['choix'] == 'Lancer des dés':
            from client.view.des_view import MenuDes
            return MenuDes(self.joueur, self.campagne)    
        if reponse['choix'] == 'Consulter les résultats des jets':
            JetDAO.consulter_tous_les_jets(self.campagne,self.joueur)
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)
        if reponse['choix'] == 'Donner un feedback':
            message = input("Quel est le feedback que vous souhaitez poster ?")
            Joueur.donner_feed_back(self.joueur,message)
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)
        if reponse['choix'] == 'Quitter la campagne':
            from client.view.accueil_jeu_view import AccueilJeuView
            return AccueilJeuView(self.joueur)
        if reponse['choix'] == 'Réaliser une action sur un donjon':
            from client.view.donjon_view import MenuDonjon
            return MenuDonjon()
        if reponse['choix'] == 'Créer une entité':
            pass
        if reponse['choix'] == 'Sauvegarder l\'état de la campagne':
            pass  
        if reponse['choix'] == 'Consulter la fiche d\'une entité':
            pass 
        if reponse['choix'] == 'Modifier la fiche d\'une entité':
            pass   
        