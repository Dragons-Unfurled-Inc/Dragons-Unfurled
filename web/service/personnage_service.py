from objets_metier import personnage
from objets_metier.entite import Entite
from objets_metier.personnage import Personnage
from web.dao.entite_dao import EntiteDAO
from web.dao.personnage_dao import PersonnageDAO


class PersonnageService():
    @staticmethod
    def add_personnage(perso:Personnage,entite:Entite):
        entite_persistee = EntiteDAO.add_entite(entite)
        perso.id_entite=entite_persistee.id_entite
        PersonnageDAO.add_personnage(perso)