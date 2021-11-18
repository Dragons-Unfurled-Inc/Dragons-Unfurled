from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.vue.abstract_vue import AbstractVue
from client.vue.joueur_vue import MenuJoueur
from client.vue.maitre_du_jeu_vue import MenuMJ
from client.vue.session import Session
from web.service.mj_service import MjService
from objets_metier.joueur import Joueur
from objets_metier.maitre_du_jeu import MaitreDuJeu
from objets_metier.utilisateur import Utilisateur
from PyInquirer import Separator, prompt
from web.dao.campagne_dao import CampagneDAO
from web.dao.maitre_du_jeu_dao import MjDAO

class AccueilJeuVue(AbstractVue):

    def __init__(self):
        self.utilisateur : Utilisateur = Session.utilisateur 
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {self.utilisateur.identifiant}, que souhaitez-vous faire ? ',
                'choices': [
                    'Rejoindre une campagne',
                    Separator(),
                    'Créer un personnage',
                    'Créer une campagne',
                    Separator(),
                    'Ecrire un feed-back',
                    'Consulter ses feed-back',
                    'Se déconnecter',
                    
                ]
            }
        ]

    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_de_jeu.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Créer un personnage':
            from client.vue.creation_personnage_vue import MenuPersonnage
            return MenuPersonnage()
            #faut ajouter la classe joueur pour le stocker je mets une val au pif pour l'instant
        
        if reponse['choix'] == 'Rejoindre une campagne': #Il faudrait charger une sauvegarde ici
            identifiant_campagne = int(input('Quel est l\'identifiant de votre campagne ?\n'))
            if identifiant_campagne in CampagneDAO.liste_id():
                campagne = CampagneDAO.get_campagne(identifiant_campagne) # liste avec l'id et le nom
                id_mj = CampagneDAO.trouve_mj(identifiant_campagne) # Ici, il faut utiliser la table Utilisateur_campagne
                liste_id_joueurs = CampagneDAO.trouve_joueurs(identifiant_campagne)
                if self.utilisateur.identifiant == id_mj:
                    personnage_joueur = MjService.trouver_personnage(campagne[0], id_mj)
                    joueur = Joueur(identifiant = self.utilisateur.identifiant, id_campagne = identifiant_campagne)
                    from client.vue.maitre_du_jeu_vue import MenuMJ
                    return MenuMJ(joueur, campagne)
                elif self.utilisateur.identifiant in liste_id_joueurs:
                    personnage_joueur = MjService.trouver_personnage(campagne[0], id_mj) 
                    personnages_joueurs = MjService.personnage_joueurs(campagne[0])
                    personnages_non_joueurs = MjService.personnage_non_joueur(campagne[0])
                    monstres = MjService.monstres(campagne[0])
                    donjons = MjService.donjons(campagne[0])
                    maitre_du_jeu = MaitreDuJeu(campagne[0],campagne[1],personnage_joueur, self.utilisateur.connecte, self.utilisateur.mot_de_passe, self.utilisateur.identifiant, self.utilisateur.est_administrateur, self.utilisateur.feed_backs,personnages_joueurs,personnages_non_joueurs,monstres,donjons)
                    from client.vue.joueur_vue import MenuJoueur
                    return MenuJoueur(maitre_du_jeu,campagne)
                else:
                    print("Vous n'êtes pas membre de cette campagne.")
                    return AccueilJeuVue()
            else:
                print("Cette campagne est introuvable.")
                return AccueilJeuVue()

        if reponse['choix'] == 'Créer une campagne':
            nom_campagne = input("Ecrivez un nom pour votre campagne.\n")
            identifiant_campagne = MaitreDuJeuService.creer_campagne(nom_campagne) # Creer_campagne affiche l'identifiant de la campagne
            return AccueilJeuVue()
        
        if reponse['choix'] == 'Ecrire un feed-back':
            message = input("Écrivez le feed-back que vous souhaitez poster.\n")
            Utilisateur.ecrire_un_feed_back(message)
            return AccueilJeuVue()

        if reponse['choix'] == 'Consulter ses feed-back':
            Utilisateur.consulter_ses_feed_back()
            return AccueilJeuVue()
        
        if reponse['choix'] == 'Se déconnecter':
            from client.vue.deconnexion_vue import Deconnexion
            return Deconnexion()
