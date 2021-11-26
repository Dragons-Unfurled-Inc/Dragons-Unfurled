from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from client.service.maitre_du_jeu_service import MaitreDuJeuService

from web.service.utilisateur_service import UtilisateurService 

from PyInquirer import prompt


class MenuConsultation(AbstractVue):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez vous consulter :',
                'choices': [
                    'La fiche d\'un personnage joueur' ,
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
        if reponse['choix'] == 'La fiche d\'un personnage joueur':
            dict_perso = MaitreDuJeuService.dict_personnages(Session.id_campagne)
            print("Voici la liste des différents personnages:")
            print(dict_perso)
            identifiant_perso = input("Saisissez l'identifiant du personnage à consulter. \n")
            perso = UtilisateurService.trouver_perso_par_id(Session.id_campagne,identifiant_perso)
            print(perso)
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'La fiche d\'un monstre' :
            dict_monstres = MaitreDuJeuService.dict_monstres(Session.id_campagne)
            print("Voici la liste des différents monstres:")
            print(dict_monstres)
            identifiant_monstre = input("Saisissez l'identifiant du monstre à consulter. \n")
            monstre = UtilisateurService.trouver_monstre_par_id(Session.id_campagne,identifiant_monstre)
            print(monstre)
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'La fiche d\'personnage non joueur (PNJ)' :
            dict_pnj = MaitreDuJeuService.dict_pnj(Session.id_campagne)
            print("Voici la liste des différents PNJ:")
            print(dict_pnj)
            identifiant_pnj = input("Saisissez l'identifiant du personnage à consulter. \n")
            pnj = UtilisateurService.trouver_perso_par_id(Session.id_campagne,identifiant_pnj)
            print(pnj)
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()