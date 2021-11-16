from client.service.campagne_service import CampagneService
from client.view.accueil_jeu_view import AccueilJeuView
from client.view.joueur_view import MenuJoueur
from client.view.maitre_du_jeu_view import MenuMJ
from objets_metier.joueur import Joueur
from objets_metier.maitre_du_jeu import MaitreDuJeu
from view.session import Session
from PyInquirer import Separator,prompt
from view.abstract_view import AbstractView
from web.dao.campagne_dao import CampagneDAO
from web.dao.db_connection import DBConnection

class RejCampView(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'id',
                'message': 'Quel est l\'id de la campagne ? '
                
            },
            {
                'type': 'list',
                'name': 'nom',
                'message': 'Quel est le nom de la campagne ? '
    
            }
            
        ]
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/accueil_de_jeu.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        utilisateur = Session.utilisateur
        #faire un écran rejoindre une campagne pas pour la 1ere fois ensuite
        reponse = prompt(self.__questions)
        if CampagneService.est_une_campagne(reponse['id'],reponse['nom']) :
            mj_bool = (utilisateur.identifiant in CampagneDAO.trouve_mj(reponse['id']))
            CampagneService.add_util_campagne(utilisateur.identifiant,reponse['id'],mj_bool) 
            if mj_bool :
                Session.utilisateur = MaitreDuJeu(utilisateur.identifiant,reponse['id'])
                return MenuMJ()
            Session.utilisateur = Joueur(utilisateur.identifiant,reponse['id'])
            return MenuJoueur()
        return AccueilJeuView()
            