# -*- coding: utf-8 -*-
"""
* Pizza delivery prompt example
* run example by writing `python example/pizza.py` in your console
"""
from __future__ import print_function, unicode_literals

import regex
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end
            
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
                'name': 'Sagesse',
                'message': 'Quelle fce a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'F2',
                'message': 'Quelle fe a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'F3',
                'message': 'Quelle f a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'F4',
                'message': 'Quelle force a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'F5',
                'message': 'Quelle forc a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'Fo6',
                'message': 'Quelle for a votre personnage ?',
                'validate': NumberValidator,
                'filter': lambda val: int(val),
                'when' : lambda answers : answers['ChoixCarac']
            },
            {
                'type': 'input',
                'name': 'F7',
                'message': 'Quelle fo a votre personnage ?',
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

answers = prompt(questions)
print('Order receipt:')
pprint(answers)
