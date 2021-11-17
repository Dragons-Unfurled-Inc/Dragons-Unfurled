from web.dao.maitre_du_jeu_dao import MjDAO

class MjService : 

    @staticmethod
    def personnage_joueurs(id_campagne):
        return MjDAO.personnages_joueurs
    
    @staticmethod
    def personnage_non_joueur(id_campagne):
        return MjDAO.personnages_non_joueurs

    @staticmethod
    def monstres(id_campagne): 
        return MjDAO.monstres
    
    @staticmethod
    def donjons(id_campagne):
        return MjDAO.donjons