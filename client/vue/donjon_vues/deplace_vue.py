from client.service.deplacement_salle_service import DeplacementSalleService
from client.service.donjon_service import DonjonService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from PyInquirer import Separator, prompt
from web.service.cellule_service import CelluleService
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
            dict_entites = MaitreDuJeuService.dict_entites()
            print("Voici la liste des différentes entités :")
            for entite in dict_entites:
                print(entite["nom_entite"], " : ", entite["id_entite"])
            identifiant_entite = input("Saisissez l'identifiant de l'entité à déplacer. \n")
            dict_salles = MaitreDuJeuService.dict_salles() 
            print("Voici la liste des salles de votre donjon :")
            for salle in dict_salles:
                print(salle["nom_salle"], " : ", salle["id_salle"])
            identifiant_salle = input("Saisissez l'identifiant de la salle dans laquelle placer l\'entité. \n")
            if DonjonService.existe_entite_campagne(identifiant_entite) and DonjonService.existe_salle_donjon(identifiant_salle):
                DonjonService.ajouter_entite_salle(identifiant_entite, identifiant_salle)  
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Déplacer une entité dans sa salle':
            dict_entites = MaitreDuJeuService.dict_entites()
            print("Voici la liste des différentes entités :")
            for entite in dict_entites:
                print(entite["nom_entite"], " : ", entite["id_entite"])
            identifiant_entite = input("Saisissez l'identifiant de l'entité à déplacer. \n")
            identifiant_salle = MaitreDuJeuService.id_salle_contenant_entite(identifiant_entite)   
            if identifiant_salle == None:
                print("L'entité entrée n'est dans aucune salle.")
            else:
                coordonnees_entite_salle = SalleService.coordonnees_entite_salle(identifiant_entite) 
                coordonnees_cellules_salle = CelluleService.coordonnees_cellules_salle(identifiant_salle)
                coordonnees_entites_salle = SalleService.coordonnees_entites_salle(identifiant_salle) 
                coordonnees_objets_salle = SalleService.coordonnees_objets_salle(identifiant_salle) 
                dimensions = SalleService.dimensions_salle(coordonnees_cellules_salle) # Cette fonction renvoie une liste contenant la largeur et la profondeur de la salle. 
                nouvelles_coordonnees_entite = DeplacementSalleService.deplacer_entite_dans_salle(dimensions, coordonnees_cellules_salle, coordonnees_entite_salle, coordonnees_entites_salle, coordonnees_objets_salle)
                if DonjonService.existe_cellules_salle(nouvelles_coordonnees_entite, identifiant_salle):  
                    DonjonService.deplacer_entite_dans_salle(identifiant_entite, identifiant_salle, nouvelles_coordonnees_entite) 
                    print("Le personnage se déplace.")
                else:
                    print("Le personnage n'a pas pu se déplacer. \nLa case était inaccessible.")
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Retirer une entité de sa salle':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
            
        if reponse['choix'] == 'Annuler':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
                    