from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from objets_metier.joueur import Joueur
from client.service.dommage import Dommage
class MenuDes(AbstractView):

    def __init__(self,joueur,campagne):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Attaquer une entité',
                    Separator(),
                    'Lancer librement des dés',
                    Separator(),
                    'Changer le mode de révélation des dés',
                    Separator(),
                    'Quitter le menu de lancer de dés',
                ]
            }
        ]
        self.joueur = joueur 
        self.campagne = campagne
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Attaquer une entité':
            perso = perso_par_id(self.campagne[0],self.joueur.identifiant)
            id_entite = input("Saisissez l'identifiant de l'entité à attaquer.")
            entite = entite_par_id(id_entite)
            Dommage.frappe(None,perso,entite)
            from client.view.des_view import MenuDes
            return MenuDes(self.joueur,self.campagne)
        if reponse['choix'] == 'Lancer librement des dés':
            pass
        if reponse['choix'] == 'Changer le mode de révélation des dés':
            self.joueur.choix_revelation = not self.joueur.choix_revelation
            from client.view.des_view import MenuDes
            return MenuDes(self.joueur,self.campagne)
        if reponse['choix'] == 'Quitter le menu de lancer de dés':
            if  est_mj_campagne(self.joueur.identifiant):
                from client.view.maitre_du_jeu_view import MenuMJ
                return MenuMJ(self.joueur,self.campagne)
            else:
                from client.view.joueur_view import MenuJoueur
                return MenuJoueur(self.joueur,self.campagne)    