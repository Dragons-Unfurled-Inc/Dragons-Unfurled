from PyInquirer import Separator, prompt, Validator, ValidationError

from view.abstract_view import AbstractView


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



class SignInView(AbstractView):

    def make_choice(self):
        from view.welcome_view import WelcomeView

        answers = prompt(questions)

        AbstractView.session.user_name = answers['pseudonyme']
        AbstractView.session.user_mdp = answers['password']
        return WelcomeView()
