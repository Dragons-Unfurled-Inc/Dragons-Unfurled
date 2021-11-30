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
            dict_objets = MaitreDuJeuService.dict_objets()
            print("Voici la liste des différents objets :")
            for objet in dict_objets:
                print(objet["nom_objet"], " : ", objet["id_objet"])
            identifiant_objet = input("Saisissez l'identifiant de l'objet à déplacer. \n")
            dict_salles = MaitreDuJeuService.dict_salles() 
            print("Voici la liste des salles de votre donjon :")
            for salle in dict_salles:
                print(salle["nom_salle"], " : ", salle["id_salle"])
            identifiant_salle = input("Saisissez l'identifiant de la salle dans laquelle placer l\'objet. \n")
            if DonjonService.existe_objet_campagne(identifiant_objet) and DonjonService.existe_salle_donjon(identifiant_salle): 
                DonjonService.ajouter_objet_salle(identifiant_objet, identifiant_salle)  
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Déplacer un objet dans sa salle':
            dict_objets = MaitreDuJeuService.dict_objets()  
            print("Voici la liste des différents objets :")
            for objet in dict_objets:
                print(objet["nom_objet"], " : ", objet["id_objet"])
            identifiant_objet = input("Saisissez l'identifiant de l'objet à déplacer. \n")
            identifiant_salle = MaitreDuJeuService.id_salle_contenant_objet(identifiant_objet)   
            if identifiant_salle == None:
                print("L'objet entré n'est dans aucune salle.")
            else:
                coordonnees_objet_salle = SalleService.coordonnees_objet_salle(identifiant_objet)   
                coordonnees_cellules_salle = CelluleService.coordonnees_cellules_salle(identifiant_salle)
                coordonnees_entites_salle = SalleService.coordonnees_entites_salle(identifiant_salle) 
                coordonnees_objets_salle = SalleService.coordonnees_objets_salle(identifiant_salle) 
                dimensions = SalleService.dimensions_salle(coordonnees_cellules_salle) # Cette fonction renvoie une liste contenant la largeur et la profondeur de la salle. 
                nouvelles_coordonnees_objet = DeplacementSalleService.deplacer_element_dans_salle(dimensions, coordonnees_cellules_salle, coordonnees_objet_salle, coordonnees_entites_salle, coordonnees_objets_salle)
                if DonjonService.existe_cellules_salle(nouvelles_coordonnees_objet, identifiant_salle):  
                    DonjonService.deplacer_objet_dans_salle(identifiant_objet, identifiant_salle, nouvelles_coordonnees_objet)  
                    print("L'objet est déplacé.")
                else:
                    print("L'objet n'a pas pu être déplacé. \nLa case était inaccessible.")
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Retirer un objet de sa salle':
            dict_objets = MaitreDuJeuService.dict_objets()  
            print("Voici la liste des différents objets :")
            for objet in dict_objets:
                print(objet["nom_objet"], " : ", objet["id_objet"])
            identifiant_objet = input("Saisissez l'identifiant de l'objet à retirer de sa salle. \n")
            identifiant_salle = MaitreDuJeuService.id_salle_contenant_objet(identifiant_objet)   
            if identifiant_salle == None:
                print("L'objet entré n'est dans aucune salle.")
            else:
                MaitreDuJeuService.retirer_objet_salle(identifiant_objet)
                print("L'objet a été retiré de sa salle.")
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
                dimensions = SalleService.dimensions_salle(coordonnees_cellules_salle) 
                nouvelles_coordonnees_entite = DeplacementSalleService.deplacer_element_dans_salle(dimensions, coordonnees_cellules_salle, coordonnees_entite_salle, coordonnees_entites_salle, coordonnees_objets_salle, identifiant_entite, identifiant_salle)
                if DonjonService.existe_cellules_salle(nouvelles_coordonnees_entite, identifiant_salle):  
                    DonjonService.deplacer_entite_dans_salle(identifiant_entite, identifiant_salle, nouvelles_coordonnees_entite) 
                    print("Le personnage se déplace.")
                else:
                    print("Le personnage n'a pas pu se déplacer. \nLa case était inaccessible.")
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Retirer une entité de sa salle':
            dict_entites = MaitreDuJeuService.dict_entites()
            print("Voici la liste des différentes entités :")
            for entite in dict_entites:
                print(entite["nom_entite"], " : ", entite["id_entite"])
            identifiant_entite = input("Saisissez l'identifiant de l'entité à retirer de sa salle. \n")
            identifiant_salle = MaitreDuJeuService.id_salle_contenant_entite(identifiant_entite)   
            if identifiant_salle == None:
                print("L'entité entrée n'est dans aucune salle.")
            else:
                MaitreDuJeuService.retirer_entite_salle(identifiant_entite)
                print("L'entité a été retirée de sa salle.")
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
            
        if reponse['choix'] == 'Annuler':
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()
                    