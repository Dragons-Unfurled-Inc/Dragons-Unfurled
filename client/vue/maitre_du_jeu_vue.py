from client.service.campagne_service import CampagneService
from client.service.donjon_service import DonjonService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from client.vue.suppr_vue.suppr_enti_vue import SupprEntiVue
from objets_metier.joueur import Joueur
from objets_metier.maitre_du_jeu import MaitreDuJeu
from pydantic import main
from PyInquirer import Separator, prompt
from objets_metier.personnage import Personnage
from web.dao.jet_dao import JetDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO


class MenuMJ(AbstractVue):


    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {Session.utilisateur.identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Créer un donjon',
                    'Réaliser une action sur un donjon',
                    'Regarder le contenu de tous ses donjons',
                    'Créer une entité',
                    'Ajouter une entité',
                    'Supprimer une entité',
                    'Consulter la fiche d\'une entité',
                    'Modifier la fiche d\'une entité',
                    'Créer un monstre',
                    #'Consulter la liste des personnages',
                    Separator(),
                    'Lancer des dés',
                    'Consulter les jets',
                    Separator(),
                    'Sauvegarder l\'état de la campagne',
                    'Quitter la campagne',
                    
                ]
            }
        ]
        self.joueur = Session.utilisateur
        self.id_campagne = Session.id_campagne
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_maitre_du_jeu.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        
        if reponse['choix'] == 'Ajouter une entité':
            from client.vue.ajout_vue.ajout_enti_vue import AjoutEntiVue
            return AjoutEntiVue()  
            

        if reponse['choix'] == 'Supprimer une entité':
            from client.vue.suppr_vue.suppr_enti_vue import SupprEntiVue
            return SupprEntiVue(self.joueur)
        
        if reponse['choix'] == 'Créer un donjon':
            nom_donjon = input("Saisissez le nom du donjon à créer. \n")
            x = int(input("Saisissez la largeur de la salle initiale. \n"))
            y = int(input("Saisissez la profondeur de la salle initiale. \n"))
            donjon = DonjonService.construire_donjon(nom_donjon, x, y)
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()

        if reponse['choix'] == 'Regarder le contenu de tous ses donjons':
            MaitreDuJeuService.voir_les_donjons()
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'Lancer des dés':
            from client.vue.des_vue import MenuDes
            return MenuDes()    
        
        if reponse['choix'] == 'Consulter les résultats des jets':
            JetDAO.consulter_tous_les_jets(self.campagne,self.joueur)
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'Quitter la campagne':
            from client.vue.accueil_jeu_vue import AccueilJeuVue
            return AccueilJeuVue()
        
        if reponse['choix'] == 'Réaliser une action sur un donjon':
            dict_donjons = DonjonService.dict_donjons()
            print("Voici les donjons disponibles:")
            for donjon in dict_donjons:
                print(donjon["nom_donjon"],' : ',donjon["id_donjon"])
            id_donjon = input("Saisissez l'identifiant du donjon souhaité.")
            existe_donjon = DonjonService.existe_donjon_campagne(id_donjon)
            if existe_donjon:
                Session.id_donjon = id_donjon       
                from client.vue.donjon_vue import MenuDonjon
                return MenuDonjon()
            else:
                print("L'identifiant du donjon saisi est introuvable.")
                from client.vue.maitre_du_jeu_vue import MenuMJ
                return MenuMJ()
        
        if reponse['choix'] == 'Créer un monstre':
                from client.vue.creation_monstre_vue import MenuMonstre
                return MenuMonstre()
            
        if reponse['choix'] == 'Sauvegarder l\'état de la campagne':
            CampagneService.sauvegarder() 
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
        
        if reponse['choix'] == 'Consulter la fiche d\'une entité':
            from client.vue.consulter_vue import MenuConsultation
            return MenuConsultation()

        if reponse['choix'] == 'Modifier la fiche d\'une entité':
            message = input("Voulez-vous modifier la fiche d'un personnage ? Saisissez Oui ou Non")
            if message == "Non":
                id_monstre = input("Saisissez l'identifiant du monstre à consulter")
                monstre = MaitreDuJeuService.trouve_entite(id_monstre)
                MaitreDuJeu.modifier_monstre(monstre)
                
            if message == "Oui":    
                id_personnage = input("Saisissez l'identifiant du personnage à consulter")
                perso = MaitreDuJeuService.trouve_entite(id_personnage)
                MaitreDuJeu.modifier_personnage(perso)  
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
