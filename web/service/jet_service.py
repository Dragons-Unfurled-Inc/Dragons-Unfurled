from web.dao.jet_dao import JetDAO

class JetService : 

    @staticmethod
    def add_jet(jet, username, choix_revel):
        JetDAO.add_jet(jet, username, choix_revel)