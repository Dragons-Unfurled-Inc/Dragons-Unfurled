from client.service.donjon_service import DonjonService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.monstre_service import MonstreService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from objets_metier.donjon import Donjon
from objets_metier.maitre_du_jeu import MaitreDuJeu
from objets_metier.salle import Salle
from PyInquirer import Separator, prompt
from web.service.salle_service import SalleService


class MenuAjout(AbstractVue):
    
    def __init__(self):

        utilisateur = Session.utilisateur
        id_campagne = Session.id_campagne
        id_donjon = Session.id_donjon


        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {utilisateur.identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Ajouter un objet de Donjon et Dragons 5e édition prédéfinit',
                    'Ajouter une entité de la campagne au donjon',
                    'Créer et ajouter un objet',
                    'Placer et/ou déplacer tous les joueurs dans une salle',
                    Separator(),
                    'Annuler',
                    
                ]
            }    
        ]
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/ecran_donjon.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())
         
    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Créer et ajouter un objet':
            nom_objet = input("Saisissez le nom (en anglais) de l'objet à ajouter. L'objet doit être présent dans D&D 5eme edition. \n")
            DonjonService.ajouter_objet_donjon(nom_objet,self.donjon)
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Ajouter un objet de Donjon et Dragons 5e édition prédéfinit':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Ajouter une entité de la campagne au donjon':
            dict_entites = MaitreDuJeuService.dict_entites()
            print("Voici la liste des différentes entités :")
            for entite in dict_entites:
                print(entite)
            identifiant_entite = input("Saisissez l'identifiant de l'entité à ajouter. \n")
            dict_salles = MaitreDuJeuService.dict_salles()
            print("Voici la liste des salles de votre donjon :")
            for salle in dict_salles:
                print(salle)
            identifiant_salle = input("Saisissez l'identifiant de la salle dans laquelle ajouter l\'entité. \n")
            if DonjonService.existe_entite_campagne(identifiant_entite) and DonjonService.existe_salle_donjon(identifiant_salle):
                DonjonService.ajouter_entite_salle(identifiant_entite, identifiant_salle) 
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Placer et/ou déplacer tous les joueurs dans une salle':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Annuler':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
                    