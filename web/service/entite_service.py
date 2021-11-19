from os import stat
from web.dao.entite_dao import EntiteDAO

class EntiteService : 

    @staticmethod
    def entite_par_id(id_entite):
        return EntiteDAO.entite_par_id(id_entite)