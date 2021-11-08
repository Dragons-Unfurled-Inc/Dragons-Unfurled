from web.dao.campagne_dao import CampagneDAO

class CampagneService():

    @staticmethod
    def add_campagne(nom_campagne):
        CampagneDAO.add_campagne(nom_campagne)
