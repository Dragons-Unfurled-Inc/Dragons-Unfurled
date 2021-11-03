from PyInquirer import Separator, prompt


from client.view.abstract_view import AbstractView

from client.view.session import Session

class MenuJoueur(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().user_name} que souhaitez-vous faire ?',
                'choices': [
                    'Modifier la fiche d\'un personnage',
                    Separator(),
                    'Consulter la fiche d\'un personnage',
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
    
    def display_info(self):
        with open('dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Modifier la fiche d\'un personnage':
            pass
        if reponse['choix'] == 'Consulter la fiche d\'un personnage':
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
        
