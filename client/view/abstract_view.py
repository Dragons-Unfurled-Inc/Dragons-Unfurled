from abc import ABC, abstractmethod

from client.view.session import Session


class AbstractView(ABC):
    """
    Cette classe est la classe mère de toutes nos vues."""

    @abstractmethod
    def display_info(self): # détermine l'affichage en console
        pass

    @abstractmethod
    def make_choice(self): # gère les choix de l'utilisateur et l'envoie vers une autre page
        pass
