from client.vue.abstract_vue import AbstractVue
from PyInquirer import prompt
from objets_metier.maitre_du_jeu import MaitreDuJeu
from client.vue.session import Session
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from web.service.utilisateur_service import UtilisateurService 


class MenuConsultation(AbstractVue):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez vous consulter :',
                'choices': [
                    'La fiche d\'un joueur' ,
                    'La fiche d\'un monstre' , 
                    'La fiche d\'personnage non joueur (PNJ)'
                ]
            }
        ]
        self.joueur = Session.utilisateur 
        self.id_campagne = Session.id_campagne
            
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'La fiche d\'un joueur':
            dict_enti = MaitreDuJeuService.dict_entites(Session.id_campagne)
            print("Voici la liste des différentes entités :")
            print(dict_enti)
            identifiant_perso = input("Saisissez l'identifiant du personnage à consulter. \n")
            perso = UtilisateurService.trouver_perso_par_id(Session.id_campagne,identifiant_perso)
            print(perso)
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'La fiche d\'un monstre' :
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'La fiche d\'personnage non joueur (PNJ)' :
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()