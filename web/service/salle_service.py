from objets_metier.salle import Salle
from web.dao.salle_dao import SalleDAO

class SalleService():

    @staticmethod
    def add_salle(id_donjon : int, coordonnees_salle_x : int, coordonnees_salle_y : int, salle : Salle): 
        SalleDAO.add_salle(id_donjon, coordonnees_salle_x , coordonnees_salle_y, salle)
        for i in range(salle.coordonnees_salle):
            None
