from client.service.campagne_service import CampagneService
from client.service.joueur_service import JoueurService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from objets_metier.utilisateur import Utilisateur
from PyInquirer import Separator, prompt


class AccueilJeuVue(AbstractVue):

    def __init__(self):
        self.utilisateur: Utilisateur = Session.utilisateur 
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f'Bonjour {self.utilisateur.identifiant}, que souhaitez-vous faire ? ',
                'choices': [
                    'Rejoindre une campagne',
                    'Créer une campagne',
                    Separator(),
                    'Consulter les identifiants de ses entités',
                    'Créer un personnage',
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
        
        if reponse['choix'] == 'Rejoindre une campagne': 
            identifiant_campagne = int(input('Quel est l\'identifiant de votre campagne ?\n'))
            if identifiant_campagne in CampagneService.liste_id():
                id_mj = CampagneService.trouve_mj(identifiant_campagne) 
                liste_id_joueurs = CampagneService.trouve_joueurs(identifiant_campagne)
                if self.utilisateur.identifiant == id_mj:
                    from client.vue.maitre_du_jeu_vue import MenuMJ
                    Session.id_campagne = identifiant_campagne
                    return MenuMJ()
                elif self.utilisateur.identifiant in liste_id_joueurs:
                    from client.vue.joueur_vue import MenuJoueur
                    Session.id_campagne = identifiant_campagne
                    return MenuJoueur()
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

        if reponse['choix'] == 'Consulter les identifiants de ses entités':
            liste_dict_perso = JoueurService.consulter_entites()
            for ligne in liste_dict_perso:
                print(ligne["nom_entite"], " : ", ligne["id_entite"])
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
