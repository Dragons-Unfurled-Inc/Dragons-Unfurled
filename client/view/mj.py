from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView

from client.view.session import Session

class MenuMJ(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().user_name} que souhaitez-vous faire ?',
                'choices': [
                    'Ajouter ou supprimer un personnage',
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
    
    def display_info(self):
        with open('dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Ajouter ou supprimer un personnage':
            pass
        if reponse['choix'] == 'Créer un donjon':
            pass
        if reponse['choix'] == 'Lancer des dés':
            from client.view.des import MenuDes
            return MenuDes()    
        if reponse['choix'] == 'Consulter les résultats des jets':
            pass
        if reponse['choix'] == 'Donner un feedback':
            pass
        if reponse['choix'] == 'Quitter la campagne':
            from client.view import start_view
            return start_view()
        if reponse['choix'] == 'Réaliser une action sur un donjon':
            from client.view.donjon import MenuDonjon
            return MenuDonjon()
        if reponse['choix'] == 'Créer une entité':
            pass
        if reponse['choix'] == 'Sauvegarder l\'état de la campagne':
            pass  
        if reponse['choix'] == 'Consulter la fiche d\'une entité':
            pass 
        if reponse['choix'] == 'Modifier la fiche d\'une entité':
            pass   
        