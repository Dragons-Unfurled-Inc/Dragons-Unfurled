from PyInquirer import Separator, prompt

from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from client.service.dommage import Dommage

from objets_metier.joueur import Joueur
from objets_metier.jet import Jet
from objets_metier.des import Des
from web.dao.utilisateur_dao import UtilisateurDAO

from web.service.jet_service import JetService
from web.service.mj_service import MjService
from web.service.entite_service import EntiteService

class MenuDes(AbstractVue):

    def __init__(self):
        self.joueur = Session.utilisateur
        self.id_campagne = Session.id_campagne
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {self.joueur.identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Attaquer une entité',
                    Separator(),
                    'Lancer librement des dés',
                    Separator(),
                    'Quitter le menu de lancer de dés',
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
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions[0])

        if reponse['choix'] == 'Attaquer une entité':
            perso = UtilisateurDAO.trouver_perso(self.id_campagne,self.joueur.identifiant)
            id_entite = int(input("Saisissez l'identifiant de l'entité à attaquer."))
            entite = EntiteService.entite_par_id(id_entite)
            Dommage.frappe(None,perso,entite)
            from client.vue.des_vue import MenuDes
            return MenuDes()

        if reponse['choix'] == 'Lancer librement des dés':
            nb_des = int(input("Saisissez le nombre de dés que vous souhaitez. \n"))
            liste_des = []
            for i in range(1, nb_des + 1):
                nb_face = input("Saissisez le nombre de face du dés n°" + str(i) + "\n")
                valeur_des = input("Saissisez la valeur du dés n°" +  str(i) + "\n")
                liste_des.append(Des(nb_face = nb_face, valeur_des = valeur_des))
            jet = Jet(liste_des = liste_des)
            Jet.lancer_des(jet)
            print(jet)
            print("La valeur de votre jet est : ", jet.valeur_jet)
            revelation = prompt(self.__questions[1])["choix_revel"]
            JetService.add_jet(jet, self.joueur.identifiant, revelation)
            from client.vue.des_vue import MenuDes
            return MenuDes()

        if reponse['choix'] == 'Quitter le menu de lancer de dés':
            if MjService.est_mj_campagne(self.id_campagne, self.joueur.identifiant):
                from client.vue.maitre_du_jeu_vue import MenuMJ
                return MenuMJ()
            else:
                from client.vue.joueur_vue import MenuJoueur
                return MenuJoueur()    
