from objets_metier.entite import Entite
from objets_metier.monstre import Monstre
from web.dao.entite_dao import EntiteDAO
from web.dao.monstre_dao import MonstreDAO
from web.dao.attaque_dao import AttaqueDAO
from web.dao.capacite_dao import CapaciteDAO
from web.dao.langage_dao import LangageDAO


class MonstreService():
    @staticmethod
    def add_monstre(monstre : Monstre):
        entite = Entite(monstre.id_joueur, monstre.id_entite, monstre.caracteristiques_entite,monstre.objets)
        entite_persistee = EntiteDAO.add_entite(entite)
        AttaqueDAO.add_attaque(entite_persistee)
        CapaciteDAO.add_capacite(entite_persistee)
        LangageDAO.add_langage(entite_persistee)
        monstre = Monstre(monstre.type, monstre.id_joueur, entite.id_entite, monstre.caracteristiques_entite, monstre.objets)
        MonstreDAO.add_personnage(monstre)