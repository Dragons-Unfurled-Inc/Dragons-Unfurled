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
