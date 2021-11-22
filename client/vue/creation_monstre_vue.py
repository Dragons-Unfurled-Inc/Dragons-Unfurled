from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from PyInquirer import Validator, ValidationError
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
import requests as req
from objets_metier.maitre_du_jeu import MaitreDuJeu


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre, s\'il vous plaît.',
                cursor_position=len(document.text))  # Move cursor to end

print('Bienvenue sur l\'écran de création de monstre')

r = req.get('https://www.dnd5eapi.co/api/races') #cette liste doit être définie ailleurs (dans le package web) plus tard 
dicraces = r.json()
listraces = [dicraces['results'][i]['name'] for i in range(dicraces['count'])]

c = req.get('https://www.dnd5eapi.co/api/classes') #cette liste doit être définie ailleurs (dans le package web) plus tard 
dicclasses = c.json()
listclasses = [dicclasses['results'][i]['name'] for i in range(dicclasses['count'])]

class MenuMonstre(AbstractVue):
    
    def __init__(self, joueur = MaitreDuJeu):
        self.questions = [
            {
                'type': 'list',
                'name': 'Type',
                'message': 'Choisissez le type du monstre',
                'choices': listclasses
            },
            
            {
                'type': 'confirm',
                'name': 'ChoixCarac',
                'message': 'Voulez vous choisir vos caractéristiques ?',
                'default': False
            },
            {
                'type': 'input',
                'name': 'Force',
                'message': 'Combien de points de force a votre monstre ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Dextérité',
                'message': 'Combien de points de dextérité a votre monstre ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Constitution',
                'message': 'Combien de points de constitution a votre monstre ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Intelligence',
                'message': 'Combien de points d\'intelligence a votre monstre ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Sagesse',
                'message': 'Combien de points de sagesse a votre monstre ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Charisme',
                'message': 'Combien de points de charisme a votre monstre ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Nom',
                'message': 'Comment s\'appelle votre monstre ?',
                'default': 'Ragnar'
            }]
        self.joueur = joueur
        
    def display_info(self):
        print(f"Bonjour {Session().identifiant}, choisissez les caractéristiques de votre monstre ")

    def make_choice(self):
        reponse = prompt(self.questions)
        from client.vue.maitre_du_jeu_vue import MenuMJ
        return MenuMJ(self.joueur,self.campagne)