from web.dao.jet_dao import JetDAO

class JetService : 

    @staticmethod
    def add_jet(jet, username, choix_revel):
        JetDAO.add_jet(jet, username, choix_revel)

    @staticmethod
    def consulter_tous_les_jets(id_campagne):
        liste_jet = JetDAO.consulter_tous_les_jets(id_campagne)
        for txt in liste_jet:
            print(txt)