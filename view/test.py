# -*- coding: utf-8 -*-
"""
* Choix de perso
* run example by writing `python example/pizza.py` in your console
"""
from __future__ import print_function, unicode_literals

import regex
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

print('Bienvenue sur l\'écran de création de personnage')

listraces = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling'] 
listclasses = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

questions = [
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
        'message': 'Quelle force a votre personnage ?',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'when' : lambda answers : answers['ChoixCarac']
    },
    {
        'type': 'input',
        'name': 'Nom',
        'message': 'Comment s\'appelle votre personnage ?',
        'default': 'Ragnar'
    },
    
]

answers = prompt(questions)
print('Order receipt:')
pprint(answers)