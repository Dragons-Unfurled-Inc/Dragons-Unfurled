from web.dao.db_connection import DBConnection
from objets_metier.utilisateur import Utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO
from objets_metier.maitre_du_jeu import MaitreDuJeu

class CampagneDAO:

    @staticmethod
    def liste_noms():
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT nom_campagne as nom FROM Campagne"
                    )
                    campagne = cursor.fetchone()
                    nom_camp = campagne['nom']
        return nom_camp
        
    @staticmethod
    def get_campagne(id_campagne):   # liste avec l'id et le nom
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_campagne as id, nom_campagne as nom FROM Campagne"\
                        "WHERE id_campagne = %(id_campagne)s;"
                    ,{"id_campagne" : id_campagne})
                    campagne = cursor.fetchone()
                    id_camp = campagne['id']
                    nom_camp = campagne['nom']
        return [id_camp, nom_camp]

    @staticmethod
    def trouve_mj(id_campagne): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_campagne as id, username as nom , est_joueur as bool FROM Utilisateur_Campagne WHERE est_joueur = false;"
                    ,{"id_campagne" : id_campagne})
                    campagne = cursor.fetchall()
                    res = []
                    for dic in campagne :
                        res.append(dic['nom'])
        return res
    
    def trouve_joueurs(id_campagne): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_campagne as id, username as nom , est_joueur as bool FROM Utilisateur_Campagne WHERE est_joueur = true;"
                    ,{"id_campagne" : id_campagne})
                    campagne = cursor.fetchall()
                    res = []
                    for dic in campagne :
                        res.append(dic['nom'])
        return res

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
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_campagne) as max FROM campagne")
                    id_camp = cursor.fetchone()
                    id_camp = id_camp['max']
        return id_camp