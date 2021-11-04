from PyInquirer import Separator, prompt, Validator, ValidationError

from client.view.abstract_view import AbstractView
from client.view.session import Session


class Deconnexion():
    #def


questions = [
    {
        'type': 'input',
        'name': 'pseudonyme',
        'message': 'Quel est votre pseudonyme ?',

    },
    {
        'type': 'password',
        'name': 'mot de passe',
        'message': 'Quel est votre mot de passe ?',
        'validate': PasswordValidator
    }
]