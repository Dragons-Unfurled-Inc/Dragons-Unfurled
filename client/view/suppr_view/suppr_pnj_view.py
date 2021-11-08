from PyInquirer import prompt
from objets_metier.maitre_du_jeu import MaitreDuJeu
from client.view.abstract_view import AbstractView
from client.view.abstract_view import AbstractView

class SupprPNJView(AbstractView):
    def __init__(self, joueur:MaitreDuJeu, campagne):
        self.joueur = joueur 
        self.liste_personnages_non_joueurs = self.joueur.personnages_non_joueurs  
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voici la liste des PNJ :',
                'choices': self.liste_personnages
            }
        ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        #Mj_services.supprimer_entite(reponse)
        from client.view.maitre_du_jeu_view import MenuMJ
        return MenuMJ(self.joueur,self.campagne)