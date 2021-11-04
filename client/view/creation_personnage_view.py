from __future__ import print_function, unicode_literals
from PyInquirer import Separator, prompt
from PyInquirer import Validator, ValidationError
from client.view.abstract_view import AbstractView
from client.view.session import Session
import regex
from pprint import pprint
from objets_metier.entite import Entite
import requests as req

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre, s\'il vous plaît.',
                cursor_position=len(document.text))  # Move cursor to end

print('Bienvenue sur l\'écran de création de personnage')

r = req.get('https://www.dnd5eapi.co/api/races') #cette liste doit être définie ailleurs (dans le package web) plus tard 
dicraces = r.json()
listraces = [dicraces['results'][i]['name'] for i in range(dicraces['count'])]

c = req.get('https://www.dnd5eapi.co/api/classes') #cette liste doit être définie ailleurs (dans le package web) plus tard 
dicclasses = c.json()
listclasses = [dicclasses['results'][i]['name'] for i in range(dicclasses['count'])]

class MenuPersonnage(AbstractView):
    
    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'Classe',
                'message': 'Choisissez la classe de votre personnage',
                'choices': listclasses
            },
            {
                'type': 'list',
                'name': 'Race',
                'message': 'Choisissez la race de votre personnage',
                'choices': listraces
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
                'message': 'Combien de points de force a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Dextérité',
                'message': 'Combien de points de dextérité a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Constitution',
                'message': 'Combien de points de constitution a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Intelligence',
                'message': 'Combien de points d\'intelligence a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Sagesse',
                'message': 'Combien de points de sagesse a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Charisme',
                'message': 'Combien de points de charisme a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Nom',
                'message': 'Comment s\'appelle votre personnage ?',
                'default': 'Ragnar'
            }]
                
    def display_info(self):
        print(f"Bonjour {Session().identifiant}, choisissez les caractéristiques de votre personnage ")

    def make_choice(self):
        reponse = prompt(self.questions)
        from client.view.accueil_jeu_view import AccueilJeuView
        return AccueilJeuView()