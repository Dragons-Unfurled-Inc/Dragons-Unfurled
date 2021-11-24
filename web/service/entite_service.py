from web.dao.entite_dao import EntiteDAO

class EntiteService : 

    @staticmethod
    def entite_par_id(id_entite):
        return EntiteDAO.entite_par_id(id_entite)
    
    @staticmethod
    def modifier_carac(id_entite, carac : str ,valeur, nom_spec = None):
        return EntiteDAO.modifier_carac(id_entite, carac, valeur, nom_spec)