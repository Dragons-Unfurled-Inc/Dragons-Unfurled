
from os import curdir
from objets_metier.salle import Salle
from web.dao.cellule_dao import CelluleDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.salle_dao import SalleDAO
from web.dao.salle_objet_dao import ObjetSalleDAO


class SalleService():

    @staticmethod
    def trouve_salle(id_salle):
        return SalleDAO.trouve_salle(id_salle)

    @staticmethod
    def ajoute_salle(id_donjon : int,  salle : Salle): 
        salle_persistee = SalleDAO.add_salle(id_donjon, salle)
        for i in range(salle.coordonnees_salle_cellule[0][0], salle.coordonnees_salle_cellule[1][0]):
            for j in range(salle.coordonnees_salle_cellule[0][1], salle.coordonnees_salle_cellule[1][1]):
                CelluleDAO.add_cellule(salle_persistee.id_salle, i, j)
        if salle_persistee.objets != None : 
            ObjetSalleDAO.add_salle_objet(salle_persistee)

    @staticmethod
    def coordonnees_entite_salle(identifiant_entite):
        return EntiteDAO.coordonnees_entite(identifiant_entite) 

    @staticmethod
    def coordonnees_objet_salle(identifiant_objet):
        return EntiteDAO.coordonnees_objet(identifiant_objet) 

    @staticmethod
    def coordonnees_entites_salle(identifiant_salle):
        return EntiteDAO.coordonnees_entites(identifiant_salle) 

    @staticmethod
    def coordonnees_objets_salle(identifiant_salle):
        return EntiteDAO.coordonnees_objets_salle(identifiant_salle) 

    @staticmethod
    def dimensions_salle(coordonnees_cellules_salle):
        largeur = 1
        profondeur = 1
        for coordonnee in coordonnees_cellules_salle:
            if coordonnee[0] > largeur:
                largeur = coordonnee[0]
            if coordonnee[1] > profondeur:
                profondeur = coordonnee[1]
        return [largeur, profondeur]
    
    @staticmethod
    def modifier_salle(id_salle : int, nom_chang : str, valeur):
        return SalleDAO.modifier_salle(id_salle, nom_chang, valeur)
            
