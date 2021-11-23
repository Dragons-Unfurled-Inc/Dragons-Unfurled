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
from web.dao.utilisateur_dao import UtilisateurDAO
from web.service.entite_service import EntiteService
from web.service.jet_service import JetService
from web.service.mj_service import MjService


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
                    'Lancer le mode d\'attaque du boss en x tours',
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
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/ecran_lancer_des.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(), affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions[0])

        if reponse['choix'] == 'Attaquer une entité':
            #perso = UtilisateurDAO.trouver_perso(self.id_campagne, self.joueur.identifiant)
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
                type_attaque = input("Quel est le type de votre attaque. Entrez c pour charisme, d pour dextérité, i pour intelligence ou f pour force.")
                bonus = int(input("Entrez la valeur du bonus d'attaque que vous voulez accorder."))
                entite_recoie = EntiteService.entite_par_id(identifiant_entite_cible)
                entite_donne = EntiteService.entite_par_id(id_entite_donne_attaque)
                Dommage.frappe(entite_donne, entite_recoie, bonus, type_attaque)
            else:
                print("L'identifiant entré ne faisait pas parti des possibilités.")
            from client.vue.des_vue import MenuDes
            return MenuDes()

        if reponse['choix'] == 'Lancer le mode d\'attaque du boss en x tours':
            tours = input("Saisissez le nombre de tours que vous aurez dans cette ultime bataille.\n")
            from client.service.entete_boss_service import Entete
            from client.vue.boss_vue import MenuBoss
            Entete.lance_la_page()
            return MenuBoss(int(tours))

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
            from client.vue.des_vue import MenuDes
            return MenuDes()

        if reponse['choix'] == 'Quitter le menu de lancer de dés':
            if MjService.est_mj_campagne(self.id_campagne, self.joueur.identifiant):
                from client.vue.maitre_du_jeu_vue import MenuMJ
                return MenuMJ()
            else:
                from client.vue.joueur_vue import MenuJoueur
                return MenuJoueur()    
