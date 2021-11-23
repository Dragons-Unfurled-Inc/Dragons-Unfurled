from client.vue.abstract_vue import AbstractVue
from client.vue.joueur_vue import MenuJoueur
from PyInquirer import prompt
from web.dao.entite_dao import EntiteDAO
from web.service.utilisateur_service import UtilisateurService

from client.vue.session import Session


class ModifCaracVue(AbstractVue):

    def __init__(self):
        utilisateur = Session.utilisateur
        id_campagne = Session.id_campagne
        self.enti_perso = UtilisateurService.trouver_perso(id_campagne, utilisateur.identifiant)
        #matcher l'id entre entis et entis_camp et hop on a l'entite du joueur, ensuite faire modif enti.caracs en choixx
        self.list_choix = self.enti_perso.caracteristiques_entite.__dict__.keys() 
        self.questions = [
                {
                    'type': 'list',
                    'name': 'Nom',
                    'message': 'Que souhaitez-vous modifier ?',
                    'choices' : self.list_choix 
                },
                {
                    'type': 'input',
                    'name': 'Val',
                    'message': 'Quelle est la nouvelle valeur ?'
                }
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.questions)
        nom = reponse['Nom']
        EntiteDAO.modifier_carac(self.enti_perso.id_entite, nom,reponse['Val'])
        return MenuJoueur()
