from web.dao.campagne_dao import CampagneDAO

class CampagneService():

    @staticmethod
    def add_campagne(nom_campagne):
        id_camp = CampagneDAO.add_campagne(nom_campagne)
        return id_camp  

        
