from web.dao.cellule_dao import CelluleDAO


class CelluleService():

    @staticmethod
    def coordonnees_cellules_salle(identifiant_salle):
        return CelluleDAO.coordonnees_cellules_salle(identifiant_salle) 
            
