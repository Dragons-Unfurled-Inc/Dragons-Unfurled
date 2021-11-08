from client.view.abstract_view import AbstractView
from PyInquirer import prompt
from objets_metier.maitre_du_jeu import MaitreDuJeu



class SupprEntiView(AbstractView):

    def __init__(self,joueur:MaitreDuJeu, campagne):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez vous supprimer :',
                'choices': [
                    'Le personnage d\'un joueur' ,
                    'Un monstre' , 
                    'Un personnage non joueur (PNJ)'

                ]
            }
        ]
        self.joueur = joueur 
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'Le personnage d\'un joueur':
            from client.view.suppr_view.suppr_pers_view import SupprPersView
            return SupprPersView(self.joueur)
        if reponse['choix'] == 'Un monstre' :
            from client.view.suppr_view.suppr_mons_view import SupprMonsView
            return SupprMonsView(self.joueur)
        if reponse['choix'] == 'Un personnage non joueur (PNJ)' :
            from client.view.suppr_view.suppr_pnj_view import SupprPNJView
            return SupprPNJView(self.joueur)