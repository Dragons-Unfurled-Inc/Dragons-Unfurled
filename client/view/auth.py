from pprint import pprint

import regex
from app.client.exception.user_not_found_exception import UserNotFoundException
from prompt_toolkit.validation import ValidationError, Validator
from PyInquirer import  prompt

from app.client.view.abstract_view import AbstractView
from app.client.view.session import Session


class PasswordValidator(Validator):
    def validate(self, document):
        ok = regex.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid password',
                cursor_position=len(document.text))  # Move cursor to end


class SignInExample(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'user_name',
                'message': 'What\'s your user_name',
            },
            {
                'type': 'input',
                'name': 'password',
                'message': 'What\'s your password',
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, please choose some pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        from view.start_view import StartView
        return StartView()
