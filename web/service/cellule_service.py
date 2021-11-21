from objets_metier.salle import Salle
from web.dao.cellule_dao import CelluleDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.salle_dao import SalleDAO
from web.dao.salle_objet_dao import ObjetSalleDAO


class CelluleService():

    @staticmethod
    def coordonnees_cellules_salle(identifiant_salle):
        return CelluleDAO.coordonnees_cellules_salle(identifiant_salle) 
            
