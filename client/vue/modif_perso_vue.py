from client.vue.abstract_vue import AbstractVue
from client.vue.joueur_vue import MenuJoueur
from client.vue.session import Session

from web.service.entite_service import EntiteService
from web.service.utilisateur_service import UtilisateurService

from PyInquirer import prompt


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
        self.questions_spec = [
                {
                    'type': 'input',
                    'name': 'Att',
                    'message': 'Quel est le nom de l\'attaque que vous souhaitez modifier ?',
                    'when' :  self.questions[0] == "attaques"
                }, 
                {
                    'type': 'input',
                    'name': 'Cap',
                    'message': 'Quel est le nom de la capacité que vous souhaitez modifier ?',
                    'when' :  self.questions[0] == "capacites"
                }, 
                {
                    'type': 'input',
                    'name': 'Lang',
                    'message': 'Quel est le nom du langage que vous souhaitez modifier ?',
                    'when' :  self.questions[0] == "languages"
                }, 
        ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.questions)
        nom = reponse['Nom']
        if nom == "attaques": 
            nom_spec = prompt(self.questions_spec)
            EntiteService.modifier_carac(self.enti_perso.id_entite, nom,reponse['Val'], nom_spec = nom_spec['Att'])
        if nom == "capacites": 
            EntiteService.modifier_carac(self.enti_perso.id_entite, nom,reponse['Val'], nom_spec = nom_spec['Cap'])
        if nom == "languages": 
            EntiteService.modifier_carac(self.enti_perso.id_entite, nom,reponse['Val'], nom_spec = nom_spec['Lang'])
        else : 
            EntiteService.modifier_carac(self.enti_perso.id_entite, nom,reponse['Val'])
        return MenuJoueur()
