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
                    'Ajouter ou déplacer un élément dans le donjon',
                    'Modifier un élément dans le donjon',
                    'Déplacer un élément',
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

        if reponse['choix'] == 'Ajouter un élément dans le donjon':
            message = input("Voulez-vous ajouter un objet ? Saisissez Oui ou Non")
            if message == "Oui":
                nom_objet = input("Saisissez le nom (en anglais) de l'objet à ajouter. L'objet doit être présent dans D&D 5eme edition.")
                objet = DonjonService.ajouter_objet_donjon(nom_objet,self.donjon)
                from client.vue.donjon_vue import MenuDonjon
                return MenuDonjon(self.joueur,self.campagne,self.donjon)
            if message == "Non":
                message2 =  input("Voulez-vous ajouter une entité ? Saisissez Oui ou Non")
                if message2 == "Oui":
                    liste_entites = MaitreDuJeu.liste_entites()
                    print("Voici la liste des différentes entités:")
                    for entite in liste_entites:
                        print(entite)
                    identifiant_entite = input("Saisissez l'identifiant de l'entité à ajouter")
                    DonjonService.ajouter_entite(identifiant_entite,self.joueur,self.donjon) #Cherche l'entité à partir de l'identifiant dans la liste des entités du MJ
                    from client.vue.donjon_vue import MenuDonjon
                    return MenuDonjon(self.joueur,self.campagne,self.donjon)

        if reponse['choix'] == 'Modifier un élément dans le donjon':
            pass

        if reponse['choix'] == 'Placer ou déplacer un élément dans le donjon': # Il faut une fonction pour déplacer tous les joueurs d'un coup
            message = input("Voulez-vous déplacer un objet ? Saisissez Oui ou Non")
            if message == "Oui":
                print("Voici les salles du donjon")
                DonjonService.afficher_nom_id_salles(self.donjon)
                id_salle = input("Rentrez l'identifiant de la salle contenant l'objet")
                message3 = input("Voulez-vous déplacer l'objet dans la salle ? Saisissez Oui ou Non.")
                salle = SalleService.trouve_salle(id_salle)
                if message3 == "Oui":
                    print("Voici le contenu de la salle:")
                    print(salle)
                    identifiant_objet = input("Saisissez l'identifiant de l'objet")
                    nouvelles_coordonnees = input("Saisissez sous format liste les nouvelles coordonnées de l'objet")  
                    DonjonService.deplacer_objet_dans_salle(self.donjon,identifiant_objet,nouvelles_coordonnees)
                    from client.vue.donjon_vue import MenuDonjon
                    return MenuDonjon(self.joueur,self.campagne,self.donjon)
                if message3 =="Non":
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
                    return MenuDonjon(self.joueur,self.campagne,self.donjon)

        if reponse['choix'] == 'Quitter le donjon':
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
      