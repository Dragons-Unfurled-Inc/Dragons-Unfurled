from __future__ import print_function, unicode_literals
from PyInquirer import Validator, ValidationError
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
import regex
from pprint import pprint
from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
import requests as req
from client.service.personnage_service import PersonnageService
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
from objets_metier.utilisateur import Utilisateur
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

from web.dao.entite_dao import EntiteDAO

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#f40099',  # default
    Token.Pointer: '#1f5100 bold',
    Token.Instruction: '#a2ff92 italic',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '#f7be00',
})

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre, s\'il vous plaît.',
                cursor_position=len(document.text))  # Move cursor to end

class MenuPersonnage(AbstractVue):
    
    def __init__(self):
        self.classes = PersonnageService.liste_classe()
        self.races = PersonnageService.liste_race()
        self.questions = [
            {
                'type': 'list',
                'name': 'Classe',
                'message': 'Choisissez la classe de votre personnage',
                'choices': self.classes
            },
            {
                'type': 'list',
                'name': 'Race',
                'message': 'Choisissez la race de votre personnage',
                'choices': self.races
            },
            {
                'type': 'input',
                'name': 'Lore',
                'message': 'Ecrivez le lore de votre personnage',
                'default': 'Lore'
            },
            {
                'type': 'input',
                'name': 'Nom',
                'message': 'Comment s\'appelle votre personnage ?',
                'default': 'Ragnar'
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
                'name': 'Intelligence',
                'message': 'Combien de points d\'intelligence a votre personnage ?',
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
                'name': 'Dexterite',
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
                'name': 'Sagesse',
                'message': 'Combien de points de sagesse a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            }
            ]
    def display_info(self):
        print(f"Bonjour {Session.utilisateur.identifiant}, \n Bienvenue sur l\'écran de création de personnage")

    def make_choice(self):
        reponse = prompt(self.questions) # prompt(self.questions,style=style_from_dict)
        utilisateur = Session.utilisateur
        #print(reponse)
        if reponse['ChoixCarac'] :
            carac = Caracteristique(reponse['Nom'],reponse['Force'],reponse['Intelligence'],reponse['Charisme'],reponse['Dexterite'],reponse['Constitution'],reponse['Sagesse'])
        else :
            carac = Caracteristique(reponse['Nom'])
        P=Personnage(reponse["Classe"],reponse["Race"],reponse["Lore"],utilisateur.identifiant,0,reponse["Nom"],carac) 
        EntiteDAO.add_entite(P)       
        from client.vue.accueil_jeu_vue import AccueilJeuVue
        return AccueilJeuVue()