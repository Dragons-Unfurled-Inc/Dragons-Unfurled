from client.view.abstract_view import AbstractView
from PyInquirer import prompt
from objets_metier.maitre_du_jeu import MaitreDuJeu



class AjoutEntiView(AbstractView):

    def __init__(self,joueur:MaitreDuJeu, campagne):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez vous ajouter :',
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
            from view.ajout_view.ajout_pers_view import AjoutPersView
            return AjoutPersView(self.joueur)
        
        if reponse['choix'] == 'Un monstre' :
            from view.ajout_view.ajout_mons_view import AjoutMonsView
            return AjoutMonsView(self.joueur)
        
        if reponse['choix'] == 'Un personnage non joueur (PNJ)' :
            from view.ajout_view.ajout_pnj_view import AjoutPNJView
            return AjoutPNJView(self.joueur)
        