from client.vue.session import Session
from objets_metier.caracteristique import Caracteristique
from objets_metier.monstre import Monstre
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection
from web.dao.salle_dao import SalleDAO

from objets_metier.objet import Objet
from objets_metier.salle import Salle
from objets_metier.donjon import Donjon
from objets_metier.personnage import Personnage
class DonjonDAO(metaclass=Singleton):
    
    @staticmethod    
    def ajoute_donjon(nom_donjon: str, taille_salle_donjon_x, taille_salle_donjon_y):
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO Donjon (nom_donjon, "\
                                        "id_campagne) "\
                    "VALUES "\
                    "(%(nom_donjon)s,%(id_campagne)s)"\

                , {"nom_donjon" : nom_donjon
                , "id_campagne" : id_campagne
                })
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_donjon) as max FROM Donjon")
                    res = cursor.fetchone()
                    id_donjon = res['max']
        SalleDAO.ajoute_salle_rectangulaire(id_donjon, taille_salle_donjon_x, taille_salle_donjon_y, "Salle principale", 0, 0)
            
    @staticmethod
    def dict_donjons():# Cette fonction renvoie un dictionnaire des donjons.
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_donjon, nom_donjon "\
                    "FROM Donjon "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                res = cursor.fetchall()
                if res != None:
                    liste_dict_donjons = [dict(row) for row in res] 
                else:
                    liste_dict_donjons = []
        return liste_dict_donjons

    @staticmethod
    def dict_salles():# Cette fonction renvoie un dictionnaire des donjons.
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_salle, nom_salle "\
                    "FROM Salle "\
                    "JOIN Donjon ON Donjon.id_donjon = Salle.id_donjon "
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                res = cursor.fetchall()
                if res != None:
                    liste_dict_salle = [dict(row) for row in res] 
                else:
                    liste_dict_salle = []
        return liste_dict_salle


    @staticmethod
    def existe_donjon_campagne(id_donjon):
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_donjon "\
                    "FROM Donjon "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_donjon = %(id_donjon)s)"\
                    , {"id_campagne" : id_campagne, "id_donjon" : id_donjon})
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    @staticmethod
    def existe_salle_donjon(id_salle):
        from client.vue.session import Session
        id_donjon = Session.id_donjon
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_salle "\
                    "FROM Salle "\
                    "WHERE (id_donjon = %(id_donjon)s) "\
                    "AND (id_salle = %(id_salle)s)"\
                    , {"id_donjon" : id_donjon, "id_salle" : id_salle})
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    @staticmethod
    def espace_libre_salle(x, y):
        from client.vue.session import Session
        id_donjon = Session.id_donjon
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Salle "\
                    "WHERE (id_donjon = %(id_donjon)s) "\
                    "AND (coordonnee_salle_x = %(coordonnee_salle_x)s) "\
                    "AND (coordonnee_salle_y = %(coordonnee_salle_y)s)"\
                    , {"id_donjon" : id_donjon, "coordonnee_salle_x" : x, "coordonnee_salle_y" : y})
                res = cursor.fetchone()
        if res != None:
            return False
        else : 
            return True
    
    @staticmethod
    def trouver_donjon(id_donjon):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Donjon "\
                    "WHERE (id_donjon = %(id_donjon)s)"
                    , {"id_donjon" : id_donjon})
                id_donjon = cursor.fetchone()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Salle "\
                    "WHERE (id_donjon = %(id_donjon)s) "\
                    , {"id_donjon" : id_donjon})
                salle = cursor.fecthall()
                if salle == None :
                    id_salle = []
                else:
                    id_salle = [salle[i]["id_salle"] for i in range(0, len(salle))]
        liste_salle = []
        for id_sal in id_salle: 
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Cellule "\
                        "WHERE (id_salle = %(id_salle)s) "\
                        , {"id_salle" : id_sal})
                    cellule = cursor.fetchall()
                    if cellule == None:
                        id_cellule = []
                    else :
                        id_cellule = [cellule[i]["id_cellule"] for i in range(0, len(cellule))]
            liste_obj = []
            liste_enti = []
            for id_cell in id_cellule:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT * "\
                            "FROM Objet "\
                            "WHERE (id_cellule = %(id_cellule)s) "\
                            , {"id_cellule" : id_cell})
                        objet = cursor.fetchall()
                        if objet == None :
                            id_objet = []
                        else:
                            id_objet = [objet[i]["id_objet"] for i in range(0, len(objet))]
                for i in range(0, len(id_objet)):
                    liste_obj.append(Objet(id_objet = i, nom_objet = objet[i]["nom_objet"], description_obj = objet[i]["description_obj"]))
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT id_entite"\
                            "FROM Entite "\
                            "WHERE (id_cellule = %(id_cellule)s) "\
                            , {"id_cellule" : id_cell})
                        id_enti = cursor.fetchall()
                        if id_enti == None :
                            id_entite = []
                        else:
                            id_entite = [id_enti[i]["id_objet"] for i in range(0, len(id_enti))]
                for id_ent in id_entite : 
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "SELECT * "\
                                "FROM Personnage "\
                                "WHERE (id_entite = %(id_entite)s) "\
                                , {"id_entite" : id_ent})
                            perso = cursor.fetchone()
                            if perso != None :
                                with DBConnection().connection as connection:
                                    with connection.cursor() as cursor:
                                        cursor.execute(
                                            "SELECT * "\
                                                "FROM Entite "\
                                                "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite"\
                                                "WHERE (id_entite = %(id_entite)s) "\
                                                , {"id_entite" : id_ent})
                                        enti_perso = cursor.fetchone()
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM Capacite "\
                                            "WHERE id_entite = %(id_entite)s "\
                                            , {"id_entite" : id_entite})
                                        capacite = cursor.fetchall()
                                        if capacite == None : 
                                            capacite = []
                                        else:
                                            capacite = [capacite[i]["nom_capacite"] for i in range(len(capacite))]
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM Langage "\
                                            "WHERE id_entite = %(id_entite)s"\
                                            , {"id_entite" : id_entite})
                                        langage = cursor.fetchall()
                                        if langage == None:
                                            langage =[]
                                        else:
                                            langage = [langage[i]["nom_langage"] for i in range(len(langage))]
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM  Attaque "\
                                            "WHERE id_entite = %(id_entite)s"\
                                            , {"id_entite" : id_entite})
                                        attaque = cursor.fetchall()
                                        if attaque == None :
                                            attaque = []
                                        else : 
                                            attaque = [attaque[i]["nom_attaque"] for i in range(0, len(attaque))]
                                with DBConnection().connection as connection:
                                    with connection.cursor() as cursor:
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM Entite_Objet "\
                                            "JOIN Objet ON Entite_Objet.id_objet = Objet.id_objet"\
                                            "WHERE (id_entite = %(id_entite)s) "\
                                            , {"id_entite" : id_ent})
                                        objet_perso = cursor.fetchall()
                                        if objet_perso == None :
                                            id_objet_perso = []
                                        else:
                                            id_objet_perso = [objet_perso[i]["id_objet"] for i in range(0, len(objet_perso))]
                                liste_objet_perso = [] 
                                for i in range(len(id_objet_perso)):
                                    liste_objet_perso.append(Objet(id_objet = objet_perso[i]["id_objet"], nom_objet = objet_perso[i]["nom_objet"], description_obj = objet_perso[i]["description_obj"]))
                                caract = Caracteristique(nom_entite = enti_perso["nom_entite"], force = enti_perso["force"], experience = enti_perso["experience"], intelligence = enti_perso["intelligence"], charisme = enti_perso["charisme"], dexterite = enti_perso["dexterite"], constitution = enti_perso["constitution"], vie = enti_perso["vie"], sagesse =  enti_perso["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = enti_perso["description"], classe_armure = enti_perso["classe_armure"])
                                perso = Personnage(classe = perso["classe"], race = perso["race"], lore = perso["lore"], id_joueur = enti_perso["username"], id_entite = enti_perso["id_entite"], nom_entite = enti_perso["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet_perso)
                                liste_enti.append(perso)

                            else : 
                                with DBConnection().connection as connection:
                                    with connection.cursor() as cursor:
                                        cursor.execute(
                                        "SELECT * "\
                                        "FROM Monstre "\
                                        "WHERE (id_entite = %(id_entite)s) "\
                                        , {"id_entite" : id_ent})
                                        perso = cursor.fetchone()
                                with DBConnection().connection as connection:
                                    with connection.cursor() as cursor:
                                        cursor.execute(
                                            "SELECT * "\
                                                "FROM Entite "\
                                                "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite"\
                                                "WHERE (id_entite = %(id_entite)s) "\
                                                , {"id_entite" : id_ent})
                                        enti_monstre = cursor.fetchone()
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM Capacite "\
                                            "WHERE id_entite = %(id_entite)s "\
                                            , {"id_entite" : id_entite})
                                        capacite = cursor.fetchall()
                                        if capacite == None : 
                                            capacite = []
                                        else:
                                            capacite = [capacite[i]["nom_capacite"] for i in range(len(capacite))]
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM Langage "\
                                            "WHERE id_entite = %(id_entite)s"\
                                            , {"id_entite" : id_entite})
                                        langage = cursor.fetchall()
                                        if langage == None:
                                            langage =[]
                                        else:
                                            langage = [langage[i]["nom_langage"] for i in range(len(langage))]
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM  Attaque "\
                                            "WHERE id_entite = %(id_entite)s"\
                                            , {"id_entite" : id_entite})
                                        attaque = cursor.fetchall()
                                        if attaque == None :
                                            attaque = []
                                        else : 
                                            attaque = [attaque[i]["nom_attaque"] for i in range(0, len(attaque))]
                                with DBConnection().connection as connection:
                                    with connection.cursor() as cursor:
                                        cursor.execute(
                                            "SELECT * "\
                                            "FROM Entite_Objet "\
                                            "JOIN Objet ON Entite_Objet.id_objet = Objet.id_objet"\
                                            "WHERE (id_entite = %(id_entite)s) "\
                                            , {"id_entite" : id_ent})
                                        objet_monstre = cursor.fetchall()
                                        if objet_monstre == None :
                                            id_objet_monstre = []
                                        else:
                                            id_objet_monstre = [objet_monstre[i]["id_objet"] for i in range(0, len(objet_monstre))]
                                liste_objet_monstre = [] 
                                for i in range(len(id_objet_monstre)):
                                    liste_objet_monstre.append(Objet(id_objet = objet_monstre[i]["id_objet"], nom_objet = objet_monstre[i]["nom_objet"], description_obj = objet_monstre[i]["description_obj"]))
                                caract = Caracteristique(nom_entite = enti_monstre["nom_entite"], force = enti_monstre["force"], experience = enti_monstre["experience"], intelligence = enti_monstre["intelligence"], charisme = enti_monstre["charisme"], dexterite = enti_monstre["dexterite"], constitution = enti_monstre["constitution"], vie = enti_monstre["vie"], sagesse =  enti_monstre["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = enti_monstre["description"], classe_armure = enti_monstre["classe_armure"])
                                monstre = Monstre(type = monstre["type"], id_joueur = enti_monstre["username"], id_entite = enti_monstre["id_entite"], nom_entite = enti_monstre["nom_entite"], caracteristiques_entite =  caract, objets = liste_objet_monstre)
                                liste_enti.append(monstre)
            liste_salle.append(Salle(id_salle = salle["id_salle"], nom_salle = salle["nom_salle"], coordonnees_salle_donjon = [0,0], coordonnees_salle_cellule = [[0,0], [1,1]], objets = liste_obj, entites = liste_enti ))
        donjon = Donjon(id_donjon = id_donjon["id_donjon"], nom_donjon = id_donjon["nom_donjon"], pieces = liste_salle)
        return donjon
                            