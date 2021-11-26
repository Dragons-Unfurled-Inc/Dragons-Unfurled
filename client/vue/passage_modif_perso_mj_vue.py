from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from client.service.maitre_du_jeu_service import MaitreDuJeuService

from web.service.utilisateur_service import UtilisateurService 

from PyInquirer import prompt




class MenuModifMJ(AbstractVue):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Voulez vous modifier :',
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
            dict_perso = MaitreDuJeuService.dict_personnages(Session.id_campagne)
            print("Voici la liste des différents personnages:")
            print(dict_perso)
            from client.vue.modif_perso_mj_vue import ModifCaracMJVue
            return ModifCaracMJVue()
        
        if reponse['choix'] == 'La fiche d\'un monstre' :
            pass
        
        if reponse['choix'] == 'La fiche d\'personnage non joueur (PNJ)' :
            dict_pnj = MaitreDuJeuService.dict_pnj(Session.id_campagne)
            print("Voici la liste des différents PNJ:")
            print(dict_pnj)
            from client.vue.modif_perso_mj_vue import ModifCaracMJVue
            return ModifCaracMJVue()