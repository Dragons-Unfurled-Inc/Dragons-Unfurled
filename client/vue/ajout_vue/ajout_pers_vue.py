from client.service.campagne_service import CampagneService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from PyInquirer import ValidationError, Validator, prompt


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
                'name': 'Nom_entite',
                'message': 'Quel est son nom ?',
                'default': 'Ragnar'
            }
            ,
            {
                'type': 'input',
                'name': 'Joueur',
                'message': 'Quel est le nom de son joueur ?'
            }
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
  
    def make_choice(self):
        reponse = prompt(self.questions)
        id_entite = reponse['ID']
        nom_entite = reponse['Nom_entite']
        id_joueur = reponse['Joueur']
        if MaitreDuJeuService.existe_entite_nom_id_joueur(nom_entite, id_entite, id_joueur): 
            MaitreDuJeuService.ajouter_entite_campagne(id_entite)  
            CampagneService.mettre_joueur_dans_campagne(id_joueur)
            print("Le personnage a bien été ajouté !")
        else:
            print("Le personnage n'a pas été ajouté. \nLes informations saisies étaient incorrectes.")
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ()

             
             