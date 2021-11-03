from PyInquirer import Separator, prompt, Validator, ValidationError
from client.view.accueil_jeu_view import AccueilJeuView

from client.view.abstract_view import AbstractView
from client.view.session import Session

class PasswordValidator(Validator):
    def validate(self, document):
        ok = len(document.text) > 5
        if not ok:
            raise ValidationError(
                message='Votre mot de passe doit faire au moins 6 caractères',
                cursor_position=len(document.text))  # Move cursor to end


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



class Authentification(AbstractView):

    def display_info(self):
        print(f"Hello {Session().identifiant}, remplissez ces informations")

    
    def make_choice(self):
        from client.view.accueil_jeu_view import AccueilJeuView

        answers = prompt(questions)

        Session.identifiant = answers['pseudonyme']
        Session.mot_de_passe = answers['mot de passe']
        return AccueilJeuView()
