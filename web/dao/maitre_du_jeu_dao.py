from client.vue.session import Session
from objets_metier.caracteristique import Caracteristique
from objets_metier.donjon import Donjon
from objets_metier.monstre import Monstre
from objets_metier.objet import Objet
from objets_metier.personnage import Personnage
from objets_metier.salle import Salle
from web.dao.db_connection import DBConnection


class MaitreDuJeuDAO:
    
    @staticmethod
    def est_mj_campagne(id_campagne, id_joueur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_campagne, username "\
                    "FROM Utilisateur_Campagne "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND est_joueur = false"\
                    , {"id_campagne" : id_campagne})
                username = cursor.fetchone()
                username = username["username"]
        return id_joueur == username

    @staticmethod
    def existe_entite_nom_id_joueur(nom_entite, id_entite, id_joueur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE (Entite.id_entite = %(id_entite)s) "\
                    "AND (nom_entite = %(nom_entite)s) "\
                    "AND (username = %(username)s);"\
                    , {"id_entite" : id_entite
                    , "nom_entite" : nom_entite
                    , "username" : id_joueur })
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    @staticmethod
    def personnages_joueurs(id_campagne): 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_joueur <> %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : "-1"})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso_joueur = []
        for i in liste_entite: 
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                entite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                enti_obj = cursor.fetchone()
                liste_objet = []
                for i in enti_obj["id_objet"]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            liste_perso_joueur.append(Personnage(personnage["classe"], personnage["race"], personnage["lore"],entite["id_joueur"], i, entite["nom_entite"], caract, liste_objet))
        return liste_perso_joueur


    @staticmethod
    def personnages_non_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso non joueurs 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_joueur = %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : "-1"})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso_non_joueur = []
        for i in liste_entite: 
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                entite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Personnage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                personnage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                enti_obj = cursor.fetchone()
                liste_objet = []
                for i in enti_obj["id_objet"]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            liste_perso_non_joueur.append(Personnage(personnage["classe"], personnage["race"], personnage["lore"],entite["id_joueur"], i, entite["nom_entite"], caract, liste_objet))
        return liste_perso_non_joueur

    @staticmethod
    def monstres(id_campagne):# Cette fonction renvoie l'ensemble des monstres 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso_joueur = []
        for i in liste_entite: 
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                entite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Monstre "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                monstre = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                capacite = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                langage = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM  Attaque"\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                attaque = cursor.fetchone()
                cursor.execute(
                    "SELECT *"\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : i})
                enti_obj = cursor.fetchone()
                liste_objet = []
                for i in enti_obj["id_objet"]:
                    cursor.execute(
                    "SELECT *"\
                    "FROM Objet "\
                    "WHERE id_objet = %(id_objet)s"\
                    , {"id_objet" : i})
                    objet = cursor.fetchone()
                    liste_objet.append(Objet(id_objet = i, nom_objet = objet[enti_obj["nom_objet"]], description_obj=objet[enti_obj["description_obj"]]))
            caract = Caracteristique(nom_entite = entite["nom_entite"], force = entite["force"], experience = entite["experience"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], vie = entite["vie"], sagesse =  entite["sagesse"], attaques= attaque["nom_attaque"], capacites = capacite["nom_capacite"], languages = langage["nom_langage"], description = entite["description"], classe_armure = entite["classe_armure"])
            liste_perso_joueur.append(Monstre(monstre["type"], entite["id_joueur"], entite["id_entite"], caract, liste_objet))
        return liste_perso_joueur

    @staticmethod
    def donjons():# Cette fonction renvoie l'ensemble des donjons
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_donjon "\
                    "FROM Donjon "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    , {"id_campagne" : id_campagne})
                liste_id_donjon = cursor.fetchall()
                liste_id_donjon = [liste_id_donjon[i]["id_donjon"] for i in range(0, len(liste_id_donjon))]
        liste_donjon = []
        for id_donjon in liste_id_donjon:
            liste_salle = []
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Donjon "\
                        "WHERE (id_donjon = %(id_donjon)s) "\
                        , {"id_donjon" : id_donjon})
                    donjon = cursor.fetchone()
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Salle "\
                        "WHERE (id_donjon = %(id_donjon)s) "\
                        , {"id_donjon" : id_donjon})
                    salle = cursor.fetchall()
                    salle = [[salle[i]["id_salle"] for i in range(0, len(salle))], [salle[i]["nom_salle"] for i in range(0, len(salle))], [salle[i]["coordonnee_salle_x"] for i in range(0, len(salle))] , [salle[i]["coordonnee_salle_y"] for i in range(0, len(salle))]]
            for k in range(len(salle[0])):
                id_salle = salle[0][k]
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT id_cellule "\
                            "FROM Cellule "\
                            "WHERE (id_salle = %(id_salle)s) "\
                            , {"id_salle" : id_salle})
                        res = cursor.fetchall()
                        id_cellules = [dict(row)["id_cellule"] for row in res] 
                liste_objet = []
                liste_enti = []
                for id_cell in id_cellules:
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
                        liste_objet.append(Objet(id_objet = i, nom_objet = objet[i]["nom_objet"], description_obj = objet[i]["description_obj"]))
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "SELECT id_entite "\
                                "FROM Entite "\
                                "WHERE (id_cellule = %(id_cellule)s) "\
                                , {"id_cellule" : id_cell})
                            id_enti = cursor.fetchall()
                            if id_enti == None :
                                id_entite = []
                            else:
                                id_entite = [id_enti[i]["id_entite"] for i in range(0, len(id_enti))]
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
                                            cursor.execute(
                                                "SELECT * "\
                                                "FROM Entite "\
                                                "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                                                "WHERE (Entite.id_entite = %(id_entite)s) "\
                                                , {"id_entite" : id_ent})
                                            enti_perso = cursor.fetchone()
                                            cursor.execute(
                                                "SELECT * "\
                                                "FROM Capacite "\
                                                "WHERE id_entite = %(id_entite)s "\
                                                , {"id_entite" : id_ent})
                                            capacite = cursor.fetchall()
                                            if capacite == None : 
                                                capacite = []
                                            else:
                                                capacite = [capacite[i]["nom_capacite"] for i in range(len(capacite))]
                                            cursor.execute(
                                                "SELECT * "\
                                                "FROM Langage "\
                                                "WHERE id_entite = %(id_entite)s"\
                                                , {"id_entite" : id_ent})
                                            langage = cursor.fetchall()
                                            if langage == None:
                                                langage =[]
                                            else:
                                                langage = [langage[i]["nom_langage"] for i in range(len(langage))]
                                            cursor.execute(
                                                "SELECT * "\
                                                "FROM  Attaque "\
                                                "WHERE id_entite = %(id_entite)s"\
                                                , {"id_entite" : id_ent})
                                            attaque = cursor.fetchall()
                                            if attaque == None :
                                                attaque = []
                                            else : 
                                                attaque = [attaque[i]["nom_attaque"] for i in range(0, len(attaque))]
                                            cursor.execute(
                                                "SELECT * "\
                                                "FROM Entite_Objet "\
                                                "JOIN Objet ON Objet.id_objet = Entite_Objet.id_objet "\
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
                                            caract = Caracteristique(nom_entite = enti_perso["nom_entite"], force = enti_perso["force"], experience = enti_perso["experience"], intelligence = enti_perso["intelligence"], charisme = enti_perso["charisme"], dexterite = enti_perso["dexterite"], constitution = enti_perso["constitution"], vie = enti_perso["vie"], sagesse =  enti_perso["sagesse"], attaques= attaque, capacites = capacite, languages = langage, description = "Nous n\'affichons pas la description ici pour ne pas surcharger.", classe_armure = enti_perso["classe_armure"])
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
                liste_salle.append(Salle(id_salle = id_salle, nom_salle = salle[1][k], coordonnees_salle_donjon = [salle[2][k], salle[3][k]], objets = liste_objet, entites = liste_enti))
            liste_donjon.append(Donjon(id_donjon = donjon["id_donjon"], nom_donjon = donjon["nom_donjon"], pieces = liste_salle))
        return liste_donjon

    @staticmethod
    def dict_entites():
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite, nom_entite "\
                    "FROM Entite "\
                    "WHERE id_campagne=%(nom)s"\
                    ,{"nom" : id_campagne}
                )
                res = cursor.fetchall()        
        liste_entite = [dict(row) for row in res]
        return liste_entite

    @staticmethod
    def dict_objets():
        id_donjon = Session.id_donjon
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_objet, nom_objet "\
                    "FROM Objet JOIN Cellule ON Objet.id_cellule = Cellule.id_cellule JOIN Salle ON Cellule.id_salle = Salle.id_salle "\
                    "WHERE id_donjon=%(nom)s"\
                    ,{"nom" : id_donjon}
                )
                res = cursor.fetchall()        
        liste_objet = [dict(row) for row in res]
        return liste_objet

    @staticmethod
    def dict_salles():
        id_donjon = Session.id_donjon
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_salle, nom_salle "\
                    "FROM Salle "\
                    "WHERE id_donjon=%(nom)s"\
                    ,{"nom" : id_donjon}
                )
                res = cursor.fetchall()        
        liste_salles = [dict(row) for row in res]
        return liste_salles

    @staticmethod
    def dict_monstres(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite, nom_entite "\
                    "FROM Monstre JOIN Entite ON Monstre.id_entite = Entite.id_entite "\
                    "WHERE id_campagne=%(nom)s"\
                    ,{"nom" : id_campagne}
                )
                res = cursor.fetchall()        
        liste_monstres = [dict(row) for row in res]
        return liste_monstres    

    @staticmethod
    def dict_personnages(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Personnage.id_entite, nom_entite "\
                    "FROM Personnage JOIN Entite ON Personnage.id_entite = Entite.id_entite "\
                    "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (username <> %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : Session.utilisateur.identifiant})
                res = cursor.fetchall()        
        liste_perso = [dict(row) for row in res]
        return liste_perso    
    
    @staticmethod
    def dict_pnj(id_campagne):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Personnage.id_entite, nom_entite "\
                    "FROM Personnage JOIN Entite ON Personnage.id_entite = Entite.id_entite "\
                    "JOIN Utilisateur_Entite ON Entite.id_entite = Utilisateur_Entite.id_entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (username = %(id_joueur)s)"\
                    , {"id_campagne" : id_campagne
                    , "id_joueur" : Session.utilisateur.identifiant})
                res = cursor.fetchall()        
        liste_pnj = [dict(row) for row in res]
        return liste_pnj
