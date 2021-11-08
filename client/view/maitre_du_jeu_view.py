from PyInquirer import Separator, prompt
from pydantic import main

from objets_metier.maitre_du_jeu import MaitreDuJeu
from client.view.abstract_view import AbstractView
from objets_metier.joueur import Joueur
from objets_metier.donjon import Donjon
from client.view.session import Session
from web.dao.jet_dao import JetDAO
from web.dao.maitre_du_jeu_dao import MjDAO
from client.view.suppr_view.suppr_enti_view import SupprEntiView
from client.service.maitre_du_jeu_service import MJService
from client.service.donjon_service import DonjonService
from client.service.campagne_service import CampagneService
            
            

class MenuMJ(AbstractView):


    def __init__(self, joueur:MaitreDuJeu, campagne):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session().identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Créer un donjon',
                    'Réaliser une action sur un donjon',
                    'Créer une entité',
                    'Ajouter une entité',
                    'Supprimer une entité',
                    'Consulter la fiche d\'une entité',
                    'Modifier la fiche d\'une entité',
                    Separator(),
                    'Lancer des dés',
                    'Consulter les jets',
                    'Donner un feedback',
                    Separator(),
                    'Sauvegarder l\état de la campagne',
                    'Quitter la campagne',
                    
                ]
            }
        ]
        self.joueur = joueur
        self.campagne = campagne
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_maitre_du_jeu.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        
        if reponse['choix'] == 'Ajouter une entité':
            from ajout_view.ajout_enti_view import AjoutEntiView
            return AjoutEntiView(self.joueur)
            
        if reponse['choix'] == 'Supprimer une entité':
            from suppr_view.suppr_enti_view import SupprEntiView
            return SupprEntiView(self.joueur)
        
        if reponse['choix'] == 'Créer un donjon':
            nom_donjon = input("Saisissez le nom du donjon à créer.")
            donjon = DonjonService.creation_donjon(nom_donjon) #doit créer au moins une salle
            MaitreDuJeu.construire_donjon(self.joueur,donjon)
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur, self.campagne)
        
        if reponse['choix'] == 'Lancer des dés':
            from client.view.des_view import MenuDes
            return MenuDes(self.joueur, self.campagne)    
        
        if reponse['choix'] == 'Consulter les résultats des jets':
            JetDAO.consulter_tous_les_jets(self.campagne,self.joueur)
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)
        
        if reponse['choix'] == 'Donner un feedback':
            message = input("Quel est le feedback que vous souhaitez poster ?")
            Joueur.donner_feed_back(self.joueur,message)
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)
        
        if reponse['choix'] == 'Quitter la campagne':
            from client.view.accueil_jeu_view import AccueilJeuView
            return AccueilJeuView(self.joueur)
        
        if reponse['choix'] == 'Réaliser une action sur un donjon':
            liste_donjon = self.joueur.donjons
            print("Voici les donjons disponibles:")
            for donjons in liste_donjon:
                print(donjons)
            id_donj = input("Saisissez l'identifiant du donjon souhaité.")   # A changer
            donjon = self.joueur.donjons[id_donj]         
            from client.view.donjon_view import MenuDonjon
            return MenuDonjon(self.joueur, self.campagne, donjon)
        
        if reponse['choix'] == 'Créer un monstre':
                from client.view.creation_monstre_view import MenuMonstre
                return MenuMonstre(self.joueur,self.campagne)
            
        if reponse['choix'] == 'Sauvegarder l\'état de la campagne':
            CampagneService.sauvegarder(self.campagne) 
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)
        
        if reponse['choix'] == 'Consulter la fiche d\'une entité':
            message = input("Voulez-vous consulter la fiche d'un personnage ? Saisissez Oui ou Non")
            if message == "Non":
                id_monstre = input("Saisissez l'identifiant du monstre à consulter")
                monstre = MJService.trouve_entite(id_monstre)
                MaitreDuJeu.consulter_monstre(monstre)
                from client.view.maitre_du_jeu_view import MenuMJ
                return MenuMJ(self.joueur,self.campagne)
            
            if message == "Oui":    
                id_personnage = input("Saisissez l'identifiant du personnage à consulter")
                perso = MJService.trouve_entite(id_personnage)
                MaitreDuJeu.consulter_personnage(perso, self.campagne[0])
                from client.view.maitre_du_jeu_view import MenuMJ
                return MenuMJ(self.joueur,self.campagne)

        if reponse['choix'] == 'Modifier la fiche d\'une entité':
            message = input("Voulez-vous modifier la fiche d'un personnage ? Saisissez Oui ou Non")
            if message == "Non":
                id_monstre = input("Saisissez l'identifiant du monstre à consulter")
                monstre = MJService.trouve_entite(id_monstre)
                MaitreDuJeu.modifier_monstre(monstre)
                
            if message == "Oui":    
                id_personnage = input("Saisissez l'identifiant du personnage à consulter")
                perso = MJService.trouve_entite(id_personnage)
                MaitreDuJeu.modifier_personnage(perso)  
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)