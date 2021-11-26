from client.vue.abstract_vue import AbstractVue

from objets_metier.maitre_du_jeu import MaitreDuJeu

from PyInquirer import prompt

class SupprMonsVue(AbstractVue):
    def __init__(self, joueur: MaitreDuJeu, campagne):
        self.joueur = joueur 
        self.liste_monstres = self.joueur.monstres  
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voici la liste des monstres :',
                'choices': self.liste_monstres
            }
        ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        #Mj_services.supprimer_entite(reponse)
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ(self.joueur,self.campagne)