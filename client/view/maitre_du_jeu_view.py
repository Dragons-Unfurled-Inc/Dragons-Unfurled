from PyInquirer import Separator, prompt
from pydantic import main

from objets_metier.maitre_du_jeu import MaitreDuJeu
from client.view.abstract_view import AbstractView
from objets_metier.joueur import Joueur
from objets_metier.donjon import Donjon
from client.view.session import Session
from web.dao.jet_dao import JetDAO
from web.dao.maitre_du_jeu_dao import MjDAO
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
                    'Ajouter ou supprimer une entité',
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
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Ajouter ou supprimer une entité':
            message = input("Voulez-vous ajouter une entité à votre campagne ? \n Saisissez Oui ou Non")
            if message == "Non":
                mes = input("Voulez-vous supprimer un personnage joueur ? \n Saisissez Oui ou Non")
                if mes == "Oui":
                    liste_personnages = self.joueur.personnages_joueurs
                    print("Voici les personnages disponibles:")
                    for personnage in liste_personnages:
                        print(personnage)
                    identifiant_entite = input("Saisissez l'identifiant du personnage à supprimer.")
                    Mj_services.supprimer_entite(identifiant_entite)
                    from client.view.maitre_du_jeu_view import MenuMJ
                    return MenuMJ(self.joueur,self.campagne)
                if mes == "Non":
                    mess = input("Voulez-vous supprimer un personnage non-joueur ? \n \n Saisissez Oui ou Non")
                    if mess == "Oui":
                        liste_pnj = self.joueur.personnages_non_joueurs
                        print("Voici les pnj disponibles:")
                        for pnj in liste_pnj:
                            print(pnj)
                        identifiant_entite = input("Saisissez l'identifiant du pnj à supprimer.")
                        Mj_services.supprimer_entite(identifiant_entite)
                        from client.view.maitre_du_jeu_view import MenuMJ
                        return MenuMJ(self.joueur,self.campagne)
                    else:
                        liste_monstres = self.joueur.monstres
                        print("Voici les monstres disponibles:")
                        for monstres in liste_monstres:
                            print(monstres)
                        identifiant_entite = input("Saisissez l'identifiant du monstre à supprimer.")
                        Mj_services.supprimer_entite(identifiant_entite)
                        from client.view.maitre_du_jeu_view import MenuMJ
                        return MenuMJ(self.joueur,self.campagne)
            if message == "Oui":
                mes = input("Voulez-vous ajouter un personnage joueur ? \n Saisissez Oui ou Non")
                if mes == "Oui":
                    identifiant_entite = input("Saisissez l'identifiant du personnage à ajouter.")
                    Mj_services.ajouter_entite(identifiant_entite) # Peut-être demander le nom pour un joueur
                    from client.view.maitre_du_jeu_view import MenuMJ
                    return MenuMJ(self.joueur,self.campagne)
                if mes == "Non":
                    mess = input("Voulez-vous ajouter un personnage non-joueur ? \n \n Saisissez Oui ou Non")
                    if mess == "Oui":
                        identifiant_entite = input("Saisissez l'identifiant du pnj à ajouter.")
                        Mj_services.ajouter_entite(identifiant_entite)
                        from client.view.maitre_du_jeu_view import MenuMJ
                        return MenuMJ(self.joueur,self.campagne)
                    else:
                        identifiant_entite = input("Saisissez l'identifiant du monstre à ajouter.")
                        Mj_services.supprimer_entite(identifiant_entite)
                        from client.view.maitre_du_jeu_view import MenuMJ
                        return MenuMJ(self.joueur,self.campagne)    
            else:
                from client.view.maitre_du_jeu_view import MenuMJ
                return MenuMJ(self.joueur,self.campagne)   
        
        if reponse['choix'] == 'Créer un donjon':
            
            nom_donjon = input("Saisissez le nom du donjon à créer.")
            import client.service.donjon_service import DonjonService
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
            from client.service.campagne_service import CampagneService
            CampagneService.sauvegarder(self.campagne) 
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)
        if reponse['choix'] == 'Consulter la fiche d\'une entité':
            message = input("Voulez-vous consulter la fiche d'un personnage ? Saisissez Oui ou Non")
            if message == "Non":
                id_monstre = input("Saisissez l'identifiant du monstre à consulter")
                monstre = Mj_services.trouve_entite(id_monstre)
                MaitreDuJeu.consulter_monstre(monstre)
                from client.view.maitre_du_jeu_view import MenuMJ
                return MenuMJ(self.joueur,self.campagne)
            if message == "Oui":    
                id_personnage = input("Saisissez l'identifiant du personnage à consulter")
                perso = Mj_services.trouve_entite(id_personnage)
                MaitreDuJeu.consulter_personnage(perso, self.campagne[0])
                from client.view.maitre_du_jeu_view import MenuMJ
                return MenuMJ(self.joueur,self.campagne)
            

        if reponse['choix'] == 'Modifier la fiche d\'une entité':
            message = input("Voulez-vous modifier la fiche d'un personnage ? Saisissez Oui ou Non")
            if message == "Non":
                id_monstre = input("Saisissez l'identifiant du monstre à consulter")
                monstre = Mj_services.trouve_entite(id_monstre)
                MaitreDuJeu.modifier_monstre(monstre)
            if message == "Oui":    
                id_personnage = input("Saisissez l'identifiant du personnage à consulter")
                perso = Mj_services.trouve_entite(id_personnage)
                MaitreDuJeu.modifier_personnage(perso)  
            from client.view.maitre_du_jeu_view import MenuMJ
            return MenuMJ(self.joueur,self.campagne)