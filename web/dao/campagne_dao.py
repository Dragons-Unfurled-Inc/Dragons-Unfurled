from web.dao.db_connection import DBConnection
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
    def add_campagne(nom_campagne : str):  #Creer_campagne affiche l'identifiant de la campagne
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Campagne (nom_campagne) "\
                        "VALUES "\
                        "(%(nom_campagne)s)"\
   
                    , { "nom_campagne" : nom_campagne}
                    )