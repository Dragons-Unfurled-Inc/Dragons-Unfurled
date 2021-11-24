from client.vue.abstract_vue import AbstractVue
from client.vue.donjon_vue import MenuDonjon
from PyInquirer import prompt
from web.dao.entite_dao import EntiteDAO
from web.service.salle_service import SalleService

from client.vue.session import Session


class ModifSalleVue(AbstractVue):

    def __init__(self, id_salle):
        utilisateur = Session.utilisateur
        id_campagne = Session.id_campagne
        self.id_salle = id_salle
        self.salle = SalleService.trouve_salle(id_salle)
        #matcher l'id entre entis et entis_camp et hop on a l'entite du joueur, ensuite faire modif enti.caracs en choixx
        self.list_choix = self.salle.__dict__.keys() 
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
                    'message': 'Quelle est la nouvelle valeur ?', 
                }
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.questions)
        nom = reponse['Nom']
        val = reponse['Val']
        SalleService.modifier_salle(self.id_salle, nom,val)
        return MenuDonjon()
