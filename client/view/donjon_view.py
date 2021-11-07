from PyInquirer import Separator, prompt

from client.view.abstract_view import AbstractView
from client.view.session import Session
from objets_metier.donjon import Donjon
from objets_metier.salle import Salle
from objets_metier.maitre_du_jeu import MaitreDuJeu

class MenuDonjon(AbstractView):

    def __init__(self, joueur:MaitreDuJeu,campagne, donjon:Donjon):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Afficher le donjon',
                    Separator(),
                    'Consulter une salle',
                    Separator(),
                    'Ajouter une salle',
                    Separator(),
                    'Modifier une salle',
                    Separator(),
                    'Ajouter un élément dans le donjon',
                    Separator(),
                    'Modifier un élément dans le donjon',
                    Separator(),
                    'Déplacer un élément',
                    Separator(),
                    'Quitter le donjon',
                    
                ]
            }    
        ]

        self.joueur = joueur
        self.campagne = campagne
        self.donjon = donjon
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Afficher le donjon':
            Donjon.afficher_donjon(self.donjon)
            from client.view.donjon_view import MenuDonjon
            return MenuDonjon(self.joueur,self.campagne,self.donjon)
        if reponse['choix'] == 'Consulter une salle':
            id_salle = input("Saisissez l'identifiant de la salle à consulter.")
            salle = Salle_service.trouve_salle(id_salle)
            print(salle)
            from client.view.donjon_view import MenuDonjon
            return MenuDonjon(self.joueur,self.campagne,self.donjon)

        if reponse['choix'] == 'Ajouter une salle':
            id_salle = input("Saisissez l'identifiant de la salle à créer.") 
            nom_salle =  input("Saisissez le nom de la salle à créer.")  
            salle = Salle(id_salle, nom_salle)
            Donjon.ajouter_salle(self.donjon, salle)
            from client.view.donjon_view import MenuDonjon
            return MenuDonjon(self.joueur,self.campagne,self.donjon)
        if reponse['choix'] == 'Modifier une salle':
            id_salle = input("Saisissez l'identifiant de la salle à consulter.")
            salle = Salle_service.trouve_salle(id_salle)
            Donjon.editer_salle(self.donjon, salle)
            from client.view.donjon_view import MenuDonjon
            return MenuDonjon(self.joueur,self.campagne,self.donjon)
        if reponse['choix'] == 'Ajouter un élément dans le donjon':
            message = input("Voulez-vous ajouter un objet ? Saisissez Oui ou Non")
            if message == "Oui":
                nom_objet = input("Saisissez le nom (en anglais) de l'objet à ajouter. L'objet doit être présent dans D&D 5eme edition.")
                objet = ObjetService.ajouter_objet_donjon(nom_objet,self.donjon)
                from client.view.donjon_view import MenuDonjon
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
                    from client.view.donjon_view import MenuDonjon
                    return MenuDonjon(self.joueur,self.campagne,self.donjon)
        if reponse['choix'] == 'Modifier un élément dans le donjon':
            pass
        if reponse['choix'] == 'Déplacer un élément dans le donjon': # Il faut une fonction pour déplacer tous les joueurs d'un coup
            message = input("Voulez-vous déplacer un objet ? Saisissez Oui ou Non")
            if message == "Oui":
                print("Voici les salles du donjon")
                DonjonService.afficher_nom_id_salles(self.donjon)
                id_salle = input("Rentrez l'identifiant de la salle contenant l'objet")
                message3 = input("Voulez-vous déplacer l'objet dans la salle ? Saisissez Oui ou Non.")
                salle = Salle_service.trouve_salle(id_salle)
                if message3 == "Oui":
                    print("Voici le contenu de la salle:")
                    print(salle)
                    identifiant_objet = input("Saisissez l'identifiant de l'objet")
                    nouvelles_coordonnees = input("Saisissez sous format liste les nouvelles coordonnées de l'objet")  
                    DonjonService.deplacer_objet_dans_salle(self.donjon,identifiant_objet,nouvelles_coordonnees)
                    from client.view.donjon_view import MenuDonjon
                    return MenuDonjon(self.joueur,self.campagne,self.donjon)
                if message3 =="Non":
                    id_salle2 = input("Rentrez l'identifiant de la salle dans laquelle vous voulez placer l'objet.")
                    salle2 = Salle_service.trouve_salle(id_salle2)
                    print("Voici le contenu de la salle contenant l'objet:")
                    print(salle)
                    identifiant_objet = input("Saisissez l'identifiant de l'objet")
                    print("Voici le contenu de la salle où vous voulez placer l'objet:")
                    print(salle2)
                    nouvelles_coordonnees = input("Saisissez sous format liste les nouvelles coordonnées de l'objet")  
                    DonjonService.deplacer_objet_salle(self.donjon,identifiant_objet,salle2,nouvelles_coordonnees) #Il faudra enlever l'objet de la première salle
                    from client.view.donjon_view import MenuDonjon
                    return MenuDonjon(self.joueur,self.campagne,self.donjon)

        if reponse['choix'] == 'Quitter le donjon':
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur, self.campagne)
      