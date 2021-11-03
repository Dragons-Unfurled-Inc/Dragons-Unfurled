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
