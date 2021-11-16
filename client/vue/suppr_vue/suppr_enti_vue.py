from client.vue.abstract_vue import AbstractVue
from PyInquirer import prompt
from objets_metier.maitre_du_jeu import MaitreDuJeu



class SupprEntiVue(AbstractVue):

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
            from client.vue.suppr_vue.suppr_pers_vue import SupprPersVue
            return SupprPersVue(self.joueur)
        if reponse['choix'] == 'Un monstre' :
            from client.vue.suppr_vue.suppr_mons_vue import SupprMonsVue
            return SupprMonsVue(self.joueur)
        if reponse['choix'] == 'Un personnage non joueur (PNJ)' :
            from client.vue.suppr_vue.suppr_pnj_vue import SupprPNJVue
            return SupprPNJVue(self.joueur)