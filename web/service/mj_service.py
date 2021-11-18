from web.dao.maitre_du_jeu_dao import MjDAO

class MjService : 
    
    @staticmethod
    def trouver_personnage(id_campagne, id_mj):
        return MjDAO.trouver_personnage(id_campagne, id_mj)
   
    @staticmethod
    def personnage_joueurs(id_campagne):
        return MjDAO.personnages_joueurs(id_campagne)
    
    @staticmethod
    def personnage_non_joueur(id_campagne):
        return MjDAO.personnages_non_joueurs(id_campagne)

    @staticmethod
    def monstres(id_campagne): 
        return MjDAO.monstres(id_campagne)
    
    @staticmethod
    def donjons(id_campagne):
        return MjDAO.donjons