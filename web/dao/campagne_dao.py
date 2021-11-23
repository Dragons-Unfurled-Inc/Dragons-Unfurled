from client.vue.session import Session
from web.dao.db_connection import DBConnection


class CampagneDAO:

    @staticmethod
    def liste_noms():
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT nom_campagne as nom FROM Campagne"
                    )
                    res = cursor.fetchall()
        liste_nom = [dict(row)["nom"] for row in res] # Nous récupérons la liste des noms à partir de res. res peut être par exemple de la forme : [RealDictRow([('nom', 'Grande partie')]), RealDictRow([('nom', 'Une campagne secondaire')])]
        return liste_nom
        
    @staticmethod 
    def liste_id():
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_campagne as id FROM Campagne"
                    )
                    res = cursor.fetchall()
        liste_nom = [dict(row)["id"] for row in res] 
        return liste_nom

    @staticmethod
    def get_campagne(id_campagne):   # liste avec l'id et le nom
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_campagne as id, nom_campagne as nom FROM Campagne "\
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
                        "SELECT id_campagne as id, username as nom , est_joueur as bool "\
                        "FROM Utilisateur_Campagne "\
                        "WHERE est_joueur = false "\
                        "AND id_campagne = %(id_campagne)s;"
                    ,{"id_campagne" : id_campagne})
                    campagne = cursor.fetchall()
                    res = []
                    for dic in campagne :
                        res.append(dic['nom'])
        return res[0]
    
    def trouve_joueurs(id_campagne): 
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT id_campagne as id, username as nom , est_joueur as bool "\
                        "FROM Utilisateur_Campagne "\
                        "WHERE est_joueur = true;"
                    ,{"id_campagne" : id_campagne})
                    campagne = cursor.fetchall()
                    res = []
                    for dic in campagne :
                        res.append(dic['nom'])
        return res

    @staticmethod  
    def creer_campagne(nom_campagne : str):  # Creer_campagne affiche l'identifiant de la campagne
        from client.vue.session import Session
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
                        "SELECT MAX(id_campagne) as max FROM campagne") # La dernière campagne ajoutée a l'id le plus élevé.
                    id_camp = cursor.fetchone()
                    id_camp = id_camp['max']
        print("Voici l'identifiant de votre campagne :\n",        id_camp)
        with DBConnection().connection as connection: # Nous sauvegardons le fait que le joueur devient MJ.
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Utilisateur_Campagne (username, "\
                                         "id_campagne, "\
                                         "est_joueur)"\
                        "VALUES "\
                        "(%(username)s,%(id_campagne)s,%(est_joueur)s)"\
   
                    , {"username" : Session.utilisateur.identifiant
                    , "id_campagne" : id_camp
                    , "est_joueur" : False
                    }
                    )
    
    @staticmethod  
    def mettre_joueur_dans_campagne(username):
        id_camp = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Utilisateur_Campagne (username, "\
                                         "id_campagne, "\
                                         "est_joueur)"\
                        "VALUES "\
                        "(%(username)s,%(id_campagne)s,%(est_joueur)s)"\

                    , {"username" : username
                    , "id_campagne" : id_camp
                    , "est_joueur" : True
                    }
                    )
    
    @staticmethod  
    def retirer_joueur_de_campagne(username):
        id_camp = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Utilisateur_campagne "\
                    "WHERE username = %(nom)s"\
                    "AND id_campagne = %(id_campagne)s;"
                    , {"id_campagne" : id_camp
                    , "nom": username})

    @staticmethod
    def trouve_entite_campagne_joueur():
        id_campagne = Session.id_campagne
        id_joueur = Session.utilisateur.identifiant
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT Entite.id_entite "\
                    "FROM Entite JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE username = %(username)s AND Entite.id_campagne = %(id_campagne)s;"\
                ,{"username": id_joueur, "id_campagne": id_campagne}
                )
                res = cursor.fetchone()
        return dict(res)["id_entite"]



