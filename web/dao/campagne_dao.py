from web.dao.configuration import DBConnection
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO
from objets_metier.maitre_du_jeu import MaitreDuJeu

class CampagneDAO:

    @staticmethod
    def liste_noms():
        return []
        
    @staticmethod
    def get_campagne(id_campagne):   # liste avec l'id et le nom
        pass
    @staticmethod
    def trouve_mj(id_campagne) -> MaitreDuJeu:
        pass 

    @staticmethod  
    def creer_campagne(nom_campagne):  #Creer_campagne affiche l'identifiant de la campagne
        pass    