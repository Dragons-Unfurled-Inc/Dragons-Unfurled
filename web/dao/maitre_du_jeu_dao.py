from objets_metier.personnage import Personnage
from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class MjDAO:

    @staticmethod
    def personnages_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso joueurs 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT username FROM UtilisateurCampagne "\
                    "WHERE id_campagne = %(id_campagne)s;"\
                    , {"id_campagne" : id_campagne})
                perso = cursor.fetchone()
#A finir 
        

    @staticmethod
    def personnages_non_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso non joueurs 
        return []

    @staticmethod
    def monstres(id_campagne):# Cette fonction renvoie l'ensemble des pmonstres 
        return []

    @staticmethod
    def donjons(id_campagne):# Cette fonction renvoie l'ensemble des donjons
        return []            
