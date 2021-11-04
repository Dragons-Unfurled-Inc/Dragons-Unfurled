from objets_metier.personnage import Personnage
from web.dao.personnage_dao import PersonnageDAO


class PersonnageService():
    @staticmethod
    def add_personnage(perso:Personnage):
        PersonnageDAO.add_personnage(perso)