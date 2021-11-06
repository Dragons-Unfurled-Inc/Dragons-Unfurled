from objets_metier.entite import Entite
from objets_metier.personnage import Personnage
from web.dao.entite_dao import EntiteDAO
from web.dao.personnage_ok_dao import PersonnageDAO
from web.dao.attaque_dao import AttaqueDAO
from web.dao.capacite_dao import CapaciteDAO
from web.dao.langage_dao import LangageDAO


class PersonnageService():
    @staticmethod
    def add_personnage(perso:Personnage):
        entite = Entite(perso.id_joueur, perso.id_entite, perso.caracteristiques_entite,perso.objets)
        entite_persistee = EntiteDAO.add_entite(entite)
        AttaqueDAO.add_attaque(entite_persistee)
        CapaciteDAO.add_capacite(entite_persistee)
        LangageDAO.add_langage(entite_persistee)
        personnage = Personnage(perso.classe, perso.race, perso.lore, perso.id_joueur, entite_persistee.id_entite, perso.nom_entite, perso.caracteristiques_entite, perso.objets)
        PersonnageDAO.add_personnage(personnage)