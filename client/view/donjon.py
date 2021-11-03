from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session

class MenuDonjon(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().user_name} que souhaitez-vous faire ?',
                'choices': [
                    'Afficher le donjon',
                    Separator(),
                    'Consulter une salle',
                    Separator(),
                    'Ajouter une salle',
                    Separator(),
                    'Modifier une salle',
                    Separator(),
                    'Ajouter un élément dans le donjon',
                    Separator(),
                    'Modifier un élément dans le donjon',
                    Separator(),
                    'Déplacer un élément',
                    Separator(),
                    'Quitter le donjon',
                    
                ]
            }
        ]
    
    def display_info(self):
        with open('dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Afficher le donjon':
            pass
        if reponse['choix'] == 'Consulter une salle':
            pass
        if reponse['choix'] == 'Ajouter une salle':
            pass    
        if reponse['choix'] == 'Modifier une salle':
            pass
        if reponse['choix'] == 'Ajouter un élément dans le donjon':
            pass
        if reponse['choix'] == 'Modifier un élément dans le donjon':
            pass
        if reponse['choix'] == 'Déplacer un élément dans le donjon':
            pass
        if reponse['choix'] == 'Quitter le donjon':
            from client.view.mj import MenuMJ
            return MenuMJ
      