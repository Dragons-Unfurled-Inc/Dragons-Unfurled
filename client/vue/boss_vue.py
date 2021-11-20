import random

from client.service.dommage import Dommage
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from objets_metier.des import Des
from objets_metier.jet import Jet
from objets_metier.joueur import Joueur
from PyInquirer import Separator, prompt
from web.dao.utilisateur_dao import UtilisateurDAO
from web.service.entite_service import EntiteService
from web.service.jet_service import JetService
from web.service.mj_service import MjService


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
                    'Attaquer une entité de la salle de bosse',
                    Separator(),
                    'Lancer librement des dés',
                    Separator(),
                    Separator(),
                    'Abandonner'
                ]
            }
        ]

    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/donjons/donjon2.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(), affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions[0])

        if reponse['choix'] == 'Attaquer une entité de la salle de bosse':
            perso = UtilisateurDAO.trouver_perso(self.id_campagne,self.joueur.identifiant)
            id_entite = int(input("Saisissez l'identifiant de l'entité à attaquer."))
            entite = EntiteService.entite_par_id(id_entite)
            Dommage.frappe(None,perso,entite)
            self.tours -= 1
            if self.tours == 0:
                from client.vue.des_vue import MenuDes
                return MenuDes()
            return MenuBoss(self.tours) 

        if reponse['choix'] == 'Lancer librement des dés':
            jet = int(input("Saisissez le jet que vous souhaitez faire. \n"))
            print("Vous avez obtenu :")
            print(random.randint(1,int(jet)))
            self.tours -= 1
            if self.tours == 0:
                from client.vue.des_vue import MenuDes
                return MenuDes()
            return MenuBoss(self.tours)  

        if reponse['choix'] == 'Abandonner':
            from client.vue.des_vue import MenuDes
            return MenuDes()   
