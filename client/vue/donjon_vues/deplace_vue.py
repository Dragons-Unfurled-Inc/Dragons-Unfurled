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


class MenuDeplace(AbstractVue):
    
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
                    'Déplacer un objet d\'une salle à une autre',
                    'Déplacer un objet dans sa salle',
                    'Retirer un objet de sa salle',
                    Separator(),
                    'Déplacer une entité d\'une salle à une autre',
                    'Déplacer une entité dans sa salle',
                    'Retirer une entité de sa salle',
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
        if reponse['choix'] == 'Déplacer un objet d\'une salle à une autre':
            print("Voici les salles du donjon")
            DonjonService.afficher_nom_id_salles(self.donjon)
            id_salle = input("Rentrez l'identifiant de la salle contenant l'objet")
            salle = SalleService.trouve_salle(id_salle)
            id_salle2 = input("Rentrez l'identifiant de la salle dans laquelle vous voulez placer l'objet.")
            salle2 = SalleService.trouve_salle(id_salle2)
            print("Voici le contenu de la salle contenant l'objet:")
            print(salle)
            identifiant_objet = input("Saisissez l'identifiant de l'objet")
            print("Voici le contenu de la salle où vous voulez placer l'objet:")
            print(salle2)
            nouvelles_coordonnees = input("Saisissez sous format liste les nouvelles coordonnées de l'objet")  
            DonjonService.deplacer_objet_salle(self.donjon,identifiant_objet,salle2,nouvelles_coordonnees) #Il faudra enlever l'objet de la première salle
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Déplacer un objet dans sa salle':
            print("Voici les salles du donjon")
            DonjonService.afficher_nom_id_salles(self.donjon)
            id_salle = input("Rentrez l'identifiant de la salle contenant l'objet")
            salle = SalleService.trouve_salle(id_salle)
            print("Voici le contenu de la salle:")
            print(salle)
            identifiant_objet = input("Saisissez l'identifiant de l'objet")
            nouvelles_coordonnees = input("Saisissez sous format liste les nouvelles coordonnées de l'objet")  
            DonjonService.deplacer_objet_dans_salle(self.donjon,identifiant_objet,nouvelles_coordonnees)
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Retirer un objet de sa salle':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Déplacer une entité d\'une salle à une autre':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Déplacer une entité dans sa salle':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Retirer une entité de sa salle':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
            
        if reponse['choix'] == 'Annuler':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
                    