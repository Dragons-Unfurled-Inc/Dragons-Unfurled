from PyInquirer import prompt
from client.service.monstre_service import MonstreService
from objets_metier.maitre_du_jeu import MaitreDuJeu
from client.vue.abstract_vue import AbstractVue
from PyInquirer import Validator, ValidationError

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre, s\'il vous plaît.',
                cursor_position=len(document.text))  # Move cursor to end

class AjoutPersVue(AbstractVue):
    
    @staticmethod
    def __init__(self):
        #self.joueur = joueur 
        self.liste_types = MonstreService.ImportListeTypes()
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
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ(self.joueur,self.campagne)