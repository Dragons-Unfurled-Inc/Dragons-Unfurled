from __future__ import print_function, unicode_literals

from pprint import pprint

import regex
import requests as req
from client.service.personnage_service import PersonnageService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session
from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
from objets_metier.utilisateur import Utilisateur
from PyInquirer import (Separator, Token, ValidationError, Validator, prompt,
                        style_from_dict)
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
            },
            {
                'type': 'input',
                'name': 'Niveau',
                'message': 'Quel est le niveau de votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Vie',
                'message': 'Combien de points de vie a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'ClasseArmure',
                'message': 'Quelle est la classe d\'armure de votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Experience',
                'message': 'Combien de points d\'experience a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Description',
                'message': 'Quelle est la description de votre personnage ?',
                'default': 'C\'est un grand aventurier.',
                'when' : lambda answers : answers['ChoixCarac']
            }
            ]
    def display_info(self):
        print(f"Bonjour {Session.utilisateur.identifiant}, \n Bienvenue sur l\'écran de création de personnage")

    def make_choice(self):
        reponse = prompt(self.questions) # prompt(self.questions,style=style_from_dict)
        utilisateur = Session.utilisateur
        #print(reponse)
        if reponse['ChoixCarac']:  
            carac = Caracteristique(nom_entite = reponse['Nom'], description = reponse['Description'], force = reponse['Force'], intelligence = reponse['Intelligence'], charisme = reponse['Charisme'], dexterite = reponse['Dexterite'], constitution = reponse['Constitution'], sagesse = reponse['Sagesse'], vie = reponse['Vie'], experience = reponse['Experience'], classe_armure = reponse['ClasseArmure'], niveau = reponse['Niveau'])
        else:  
            carac = Caracteristique(nom_entite = reponse['Nom'])
        personnage = Personnage(classe = reponse["Classe"], race = reponse["Race"], lore = reponse["Lore"], id_joueur = utilisateur.identifiant, id_entite = -1, nom_entite = reponse["Nom"], caracteristiques_entite = carac) 
        EntiteDAO.ajoute_entite(personnage)       
        from client.vue.accueil_jeu_vue import AccueilJeuVue
        return AccueilJeuVue()
