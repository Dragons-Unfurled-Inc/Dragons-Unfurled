from PyInquirer import Separator, prompt, Validator, ValidationError

from client.view.abstract_view import AbstractView
from client.view.session import Session


class Deconnexion():
    #def


questions = [
    {
        'type': 'input',
        'name': 'confirmer_deco',
        'message': 'Confirmer la déconnexion.',

    },
    {
        'type': 'password',
        'name': 'Annuler',
        'message': 'Annuler.'
    }
]