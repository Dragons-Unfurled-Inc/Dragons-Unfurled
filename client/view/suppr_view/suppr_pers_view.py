from typing import AbstractSet

from client.view.abstract_view import AbstractView

class SupprPersView(AbstractView):
    def __init__(self, joueur:MaitreDuJeu, campagne):
        self.joueur = joueur 
        self.liste_personnages = self.joueur.personnages_joueurs  
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Voici la liste des personnages :',
                'choices': self.liste_personnages
            }
        ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        Mj_services.supprimer_entite(reponse)
        from client.view.maitre_du_jeu_view import MenuMJ
        return MenuMJ(self.joueur,self.campagne)