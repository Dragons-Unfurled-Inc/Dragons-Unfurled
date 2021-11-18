from PyInquirer import prompt
from client.service.monstre_service import MonstreService
from objets_metier.maitre_du_jeu import MaitreDuJeu
from client.vue.abstract_vue import AbstractVue
from PyInquirer import Validator, ValidationError
from client.vue.session import Session
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.campagne_service import CampagneService

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre, s\'il vous plaît.',
                cursor_position=len(document.text))  # Move cursor to end

class AjoutPersVue(AbstractVue):
    
    
    def __init__(self):
        self.joueur = Session.utilisateur 
        self.questions = [
            {
                'type': 'input',
                'name': 'ID',
                'message': 'Quel est l\'ID du personnage que vous voulez ajouter ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
            },
            {
                'type': 'input',
                'name': 'Pseudo',
                'message': 'Quel est son nom ?',
                'default': 'Ragnar'
            }
            ,
            {
                'type': 'input',
                'name': 'Joueur',
                'message': 'Quel est son joueur ?'
            }
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
  
    def make_choice(self):
        reponse = prompt(self.questions)
        MaitreDuJeuService.ajouter_entite_campagne(reponse['ID'])  
        CampagneService.mettre_joueur_dans_campagne(reponse['Joueur'])
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ()