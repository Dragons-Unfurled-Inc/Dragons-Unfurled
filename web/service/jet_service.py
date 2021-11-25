from web.dao.jet_dao import JetDAO


class JetService : 

    @staticmethod
    def ajout_jet(jet, identifiant, choix_revel):
        JetDAO.ajout_jet(jet, identifiant, choix_revel) 

    @staticmethod
    def consulter_tous_les_jets(id_campagne):
        liste_jet = JetDAO.consulter_tous_les_jets(id_campagne)
        for txt in liste_jet:
            print(txt)

    @staticmethod
    def consulter_tous_les_jets_MJ(id_campagne):
        liste_jet = JetDAO.consulter_tous_les_jets_mj(id_campagne)
        for txt in liste_jet:
            print(txt)        
