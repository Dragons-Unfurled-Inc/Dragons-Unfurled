from objets_metier.donjon import Donjon
from web.dao.donjon_dao import DonjonDAO
from web.service.salle_service import SalleService

class DonjonService() :

    @staticmethod
    def add_donjon(id_campagne : int, donjon : Donjon):
        donjon_persiste = DonjonDAO.add_donjon(id_campagne, donjon)
        if donjon.pieces != None : 
            for piece in donjon.pieces : 
                SalleService.add_salle(donjon_persiste.id_donjon, piece)
            