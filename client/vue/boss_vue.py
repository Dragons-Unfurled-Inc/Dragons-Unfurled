import random

from client.service.campagne_service import CampagneService
from client.service.dommage import Dommage
from client.service.donjon_service import DonjonService
from client.service.joueur_service import JoueurService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from objets_metier.des import Des
from objets_metier.jet import Jet
from PyInquirer import Separator, prompt
from web.service.entite_service import EntiteService
from web.service.jet_service import JetService


class MenuBoss(AbstractVue):

    def __init__(self, nombre_de_tours):
        self.joueur = Session.utilisateur
        self.id_campagne = Session.id_campagne
        self.tours = nombre_de_tours
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' Il vous reste {self.tours} tours ! Qu\'allez-vous faire ?!',
                'choices': [
                    'Attaquer une entité de la salle de boss',
                    Separator(),
                    'Lancer librement des dés',
                    Separator(),
                    Separator(),
                    'Abandonner'
                ]
            },
            {
                'type': 'confirm',
                'name': 'choix_revel',
                'message': 'Voulez-vous révélez votre jet ?',
                'default': False
            }
        ]

    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/donjons/donjon2.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(), affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions[0])

        if reponse['choix'] == 'Attaquer une entité de la salle de boss':
            dict_entites = MaitreDuJeuService.dict_entites()
            print("Voici la liste des différentes entités :\n")
            for entite in dict_entites:
                print(entite["nom_entite"], " : ", entite["id_entite"])
            identifiant_entite_cible = int(input("Saisissez l'identifiant de l'entité à attaquer.\n"))
            id_mj = CampagneService.trouve_mj(self.id_campagne)
            if self.joueur.identifiant == id_mj:
                id_entite_donne_attaque = int(input("En tant que maître du jeu, vous pouvez maintenant entrer l'identifiant de l'entité attaquante.\n"))
            else:
                id_entite_donne_attaque = JoueurService.trouve_entite_campagne()
            if DonjonService.existe_entite_campagne(identifiant_entite_cible):
                type_attaque = input("Quel est le type de votre attaque. Entrez c pour charisme, d pour dextérité, i pour intelligence ou f pour force.\n")
                bonus = int(input("Entrez la valeur du bonus d'attaque que vous voulez accorder.\n"))
                entite_recoie = EntiteService.entite_par_id(identifiant_entite_cible)
                entite_donne = EntiteService.entite_par_id(id_entite_donne_attaque)
                Dommage.frappe(entite_donne, entite_recoie, bonus, type_attaque)
            else:
                print("L'identifiant entré ne faisait pas parti des possibilités.")
            self.tours -= 1
            if self.tours == 0:
                from client.vue.des_vue import MenuDes
                return MenuDes()
            return MenuBoss(self.tours) 

        if reponse['choix'] == 'Lancer librement des dés':
            nb_des = int(input("Saisissez le nombre de dés que vous souhaitez. \n"))
            liste_des = []
            for i in range(1, nb_des + 1):
                nb_faces = input("Saissisez le nombre de face du dés n°" + str(i) + "\n")
                # valeur_des = input("Saissisez la valeur du dés n°" +  str(i) + "\n")
                liste_des.append(Des(nb_face = nb_faces)) #, valeur_des = valeur_de
            jet = Jet(liste_des = liste_des)
            Jet.lancer_des(jet) 
            print("La valeur de votre jet est : ", jet.valeur_jet)
            revelation = prompt(self.__questions[1])["choix_revel"]
            JetService.add_jet(jet, self.joueur.identifiant, revelation)
            self.tours -= 1
            if self.tours == 0:
                from client.vue.des_vue import MenuDes
                return MenuDes()
            return MenuBoss(self.tours)  

        if reponse['choix'] == 'Abandonner':
            from client.vue.des_vue import MenuDes
            return MenuDes()   
