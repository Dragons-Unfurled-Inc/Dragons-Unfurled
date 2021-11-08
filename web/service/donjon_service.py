from objets_metier.donjon import Donjon
from web.dao.donjon_dao import DonjonDAO

class DonjonService() :

    @staticmethod
    def add_donjon(id_campagne : int, donjon : Donjon):
        DonjonDAO.add_donjon(id_campagne, donjon)