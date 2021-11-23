from typing import List

from objets_metier.donjon import Donjon
from objets_metier.objet import Objet
from utils.singleton import Singleton
from web.dao.cellule_dao import CelluleDAO
from web.dao.donjon_dao import DonjonDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO
from web.dao.objet_dao import ObjetDAO
from web.dao.salle_dao import SalleDAO


class DonjonService(metaclass = Singleton):

    @staticmethod
    def construire_donjon(nom_donjon: str, coordonnees_salle_donjon_x: int, coordonnees_salle_donjon_y: int):
       DonjonDAO.ajoute_donjon(nom_donjon, coordonnees_salle_donjon_x, coordonnees_salle_donjon_y)

    @staticmethod
    def editer_donjon(self, donjon : Donjon): 
       None      

    @staticmethod
    def dict_salles():
        return DonjonDAO.dict_salles()

    @staticmethod
    def trouver_donjon(id_donjon):
        return DonjonDAO.trouver_donjon(id_donjon)

    @staticmethod
    def dict_donjons():
        return DonjonDAO.dict_donjons()

    @staticmethod
    def existe_donjon_campagne(id_donjon: int):
        return DonjonDAO.existe_donjon_campagne(id_donjon)

    @staticmethod
    def existe_entite_campagne(id_entite: int):
        return EntiteDAO.existe_entite_campagne(id_entite)

    @staticmethod
    def existe_salle_donjon(id_salle: int):
        return DonjonDAO.existe_salle_donjon(id_salle)

    @staticmethod
    def espace_libre_salle(x: int, y: int): 
       return DonjonDAO.espace_libre_salle(x,y) 

    @staticmethod
    def ajouter_entite_salle(identifiant_entite: int, identifiant_salle: int): 
        return SalleDAO.ajouter_entite_salle(identifiant_entite, identifiant_salle) 

    @staticmethod
    def ajouter_entites_salle(identifiant_salle: int): 
        dictionnaire = MaitreDuJeuDAO.dict_entites()
        for entite in dictionnaire:
            SalleDAO.ajouter_entite_salle(entite["id_entite"], identifiant_salle)
    
    @staticmethod
    def ajouter_objet_salle(identifiant_salle, id_objet):
        SalleDAO.ajouter_objet_salle(identifiant_salle, id_objet) 

    @staticmethod
    def deplacer_entite_dans_salle(identifiant_entite: int, identifiant_salle: int, nouvelles_coordonnees_entite: List[int]):
        id_cellule = CelluleDAO.trouve_id_cellule(identifiant_salle, nouvelles_coordonnees_entite[0], nouvelles_coordonnees_entite[1]) 
        SalleDAO.ajouter_entite_cellule(identifiant_entite, id_cellule)

    @staticmethod
    def deplacer_objet_dans_salle(identifiant_objet: int, identifiant_salle: int, nouvelles_coordonnees_objet: List[int]):
        id_cellule = CelluleDAO.trouve_id_cellule(identifiant_salle, nouvelles_coordonnees_objet[0], nouvelles_coordonnees_objet[1]) 
        SalleDAO.ajouter_objet_cellule(identifiant_objet, id_cellule)

    @staticmethod
    def existe_cellules_salle(nouvelles_coordonnees_entite, identifiant_salle):
        id_cellule = CelluleDAO.trouve_id_cellule(identifiant_salle, nouvelles_coordonnees_entite[0], nouvelles_coordonnees_entite[1]) 
        if id_cellule == None:
            return False
        return True

    @staticmethod
    def ajouter_objet_donjon(nom_objet, description_objet):
        objet = Objet(-1, nom_objet, description_objet)
        ObjetDAO.ajouter_objet(objet)

    @staticmethod
    def ajouter_objet_et_recuperation_donjon(nom_objet, description_objet):
        objet = Objet(-1, nom_objet, description_objet)
        return ObjetDAO.ajouter_objet_et_recuperation(objet)
