from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from objets_metier.donjon import Donjon

class MenuDonjon(AbstractView):

    def __init__(self, donjon:Donjon):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
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
        self.__donjon = donjon
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Afficher le donjon':
            Donjon.afficher_donjon()
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
            from client.view.mj_view import MenuMJ
            return MenuMJ
      