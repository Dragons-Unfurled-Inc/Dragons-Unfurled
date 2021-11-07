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
                
        if reponse['choix'] == 'Modifier un élément dans le donjon':
            pass
        if reponse['choix'] == 'Déplacer un élément dans le donjon': # Il faut une fonction pour déplacer tous les joueurs d'un coup
            pass 
        if reponse['choix'] == 'Quitter le donjon':
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur, self.campagne)
      