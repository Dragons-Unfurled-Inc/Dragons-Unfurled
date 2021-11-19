from os import stat
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO

class MjService : 
    
    @staticmethod
    def est_mj_campagne(id_campagne, id_joueur):
        return MaitreDuJeuDAO.est_mj_campagne(id_campagne, id_joueur)
    
    @staticmethod
    def trouver_personnage(id_campagne, id_mj):
        return MaitreDuJeuDAO.trouver_personnage(id_campagne, id_mj)
   
    @staticmethod
    def personnage_joueurs(id_campagne):
        return MaitreDuJeuDAO.personnages_joueurs(id_campagne)
    
    @staticmethod
    def personnage_non_joueur(id_campagne):
        return MaitreDuJeuDAO.personnages_non_joueurs(id_campagne)

    @staticmethod
    def monstres(id_campagne): 
        return MaitreDuJeuDAO.monstres(id_campagne)
    
    @staticmethod
    def donjons(id_campagne):
        return MaitreDuJeuDAO.donjons