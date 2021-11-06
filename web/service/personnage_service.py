from objets_metier.entite import Entite
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from web.dao.entite_dao import EntiteDAO
from web.dao.personnage_ok_dao import PersonnageDAO
from web.dao.attaque_dao import AttaqueDAO
from web.dao.capacite_dao import CapaciteDAO
from web.dao.langage_dao import LangageDAO
from web.dao.entite_objet_dao import ObjetEntiteDAO

class PersonnageService():
    @staticmethod
    def add_personnage(perso:Personnage):
        entite = Entite(perso.id_joueur, perso.id_entite, perso.caracteristiques_entite,perso.objets)
        entite_persistee = EntiteDAO.add_entite(entite)
        print(entite_persistee)
        AttaqueDAO.add_attaque(entite_persistee)        
        CapaciteDAO.add_capacite(entite_persistee)
        LangageDAO.add_langage(entite_persistee)
        if entite_persistee.objets != None:
            ObjetEntiteDAO.add_entite_objet(entite_persistee)
        personnage = Personnage(perso.classe, perso.race, perso.lore, perso.id_joueur, entite_persistee.id_entite, perso.nom_entite, Caracteristique(perso.caracteristiques_entite['nom_entite'],perso.caracteristiques_entite['attaques'], perso.caracteristiques_entite['capacites'], perso.caracteristiques_entite['languages'], perso.caracteristiques_entite['description']), [Objet(perso.objets[i]["id_objet"], perso.objets[i]["nom_objet"],perso.objets[i]["description"]) for i in range(0, len(perso.objets))])
        print(personnage)
        PersonnageDAO.add_personnage(personnage)


