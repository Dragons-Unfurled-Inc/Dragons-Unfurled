from client.service.donjon_service import DonjonService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from objets_metier.donjon import Donjon
from objets_metier.maitre_du_jeu import MaitreDuJeu
from objets_metier.salle import Salle
from PyInquirer import Separator, prompt
from web.service.salle_service import SalleService


class MenuDonjon(AbstractVue):

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
                    'Afficher le donjon',
                    'Consulter une salle',
                    'Ajouter une salle',
                    'Modifier une salle',
                    Separator(),
                    'Ajouter un élément dans une salle du donjon',
                    'Modifier un élément dans le donjon',
                    'Déplacer ou retirer un élément',
                    Separator(),
                    'Quitter le donjon',
                    
                ]
            }    
        ]
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/ecran_donjon.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Afficher le donjon':
            Donjon.afficher_donjon()
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Consulter une salle':
            id_salle = input("Saisissez l'identifiant de la salle à consulter.")
            salle = SalleService.trouve_salle(id_salle)
            print(salle)
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Ajouter une salle':
            id_salle = input("Saisissez l'identifiant de la salle à créer.") 
            nom_salle =  input("Saisissez le nom de la salle à créer.")  
            salle = Salle(id_salle, nom_salle)
            Donjon.ajouter_salle(self.donjon, salle)
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon(self.joueur,self.campagne,self.donjon)

        if reponse['choix'] == 'Modifier une salle':
            id_salle = input("Saisissez l'identifiant de la salle à consulter.")
            salle = SalleService.trouve_salle(id_salle)
            Donjon.editer_salle(self.donjon, salle)
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon(self.joueur,self.campagne,self.donjon)

        if reponse['choix'] == 'Ajouter un élément dans une salle du donjon':
            from client.vue.donjon_vues.ajout_vue import MenuAjout
            return MenuAjout()

        if reponse['choix'] == 'Modifier un élément dans le donjon':
            pass

        if reponse['choix'] == 'Déplacer ou retirer un élément':
            from client.vue.donjon_vues.deplace_vue import MenuDeplace
            return MenuDeplace()

        if reponse['choix'] == 'Quitter le donjon':
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
      