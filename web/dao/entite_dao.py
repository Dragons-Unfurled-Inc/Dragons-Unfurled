from abc import abstractstaticmethod

import requests as req
from client.vue.session import Session
from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
from objets_metier.objet import Objet
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection
from web.dao.monstre_dao import MonstreDAO
from web.dao.personnage_dao import PersonnageDAO
from web.dao.utilisateur_entite_dao import UtilisateurEntiteDao


#le code est pas ouf mais vous avez une idée de comment faire, par contre c'est ptet plus à sa place dans le package web
class EntiteDAO:
    # @staticmethod
    # def creation_monstre(nom): 
    #     r = req.get('https://www.dnd5eapi.co/api/monsters/aboleth') 
    #     d=r.json()
    #     return(Monstre(nom,d["size"],d["alignment"],d['armor_class'],d['hit_points'],d['hit_dice'],d['speed'],d['strength'],d['dexterity'],d['constitution'],d['intelligence'],d['wisdom'],d['charisma'],d['proficiencies'],d['languages'],d['xp'])) 

    @staticmethod    
    def add_entite(enti : Entite) -> Entite:
            if enti.objets == None : 
                entite = Entite(enti.id_joueur, enti.id_entite, Caracteristique.parse_obj(enti.caracteristiques_entite))
            else:
                entite = Entite(enti.id_joueur, enti.id_entite, Caracteristique.parse_obj(enti.caracteristiques_entite), enti.objets)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Entite (nom_entite, "\
                                            "niveau,"\
                                            "experience,"\
                                            "force,"\
                                            "intelligence, "\
                                            "charisme, "\
                                            "dexterite, "\
                                            "constitution,"\
                                            "sagesse, "\
                                            "vie, "\
                                            "description,"\
                                            "classe_armure) "\
                        "VALUES "\
                        "(%(nom_entite)s,%(niveau)s,%(experience)s, %(force)s, %(intelligence)s, %(charisme)s, %(dexterite)s, %(constitution)s, %(sagesse)s,%(vie)s, %(description)s, %(classe_armure)s)"
   
                    , { "nom_entite" : entite.caracteristiques_entite.nom_entite
                    , "niveau": entite.caracteristiques_entite.niveau
                    , "experience": entite.caracteristiques_entite.experience
                    , "force": entite.caracteristiques_entite.force
                    , "intelligence": entite.caracteristiques_entite.intelligence
                    , "charisme": entite.caracteristiques_entite.charisme
                    , "dexterite": entite.caracteristiques_entite.dexterite
                    , "constitution": entite.caracteristiques_entite.constitution
                    , "sagesse": entite.caracteristiques_entite.sagesse
                    , "vie": entite.caracteristiques_entite.vie
                    , "description": entite.caracteristiques_entite.description
                    , "classe_armure": entite.caracteristiques_entite.classe_armure
                    }) 
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_entite) as max FROM Entite")
                    id_ent = cursor.fetchone()
                    id_ent = id_ent['max']
            if enti.objets == None : 
                entite_retournee = Entite(enti.id_joueur, id_ent, Caracteristique.parse_obj(enti.caracteristiques_entite))
            else:
                entite_retournee = Entite(enti.id_joueur, id_ent, Caracteristique.parse_obj(enti.caracteristiques_entite), [Objet.parse_obj(enti.objets[i]) for i in range(0, len(enti.objets))])
            return entite_retournee

    @staticmethod    
    def ajoute_entite(entite : Entite):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Entite (nom_entite, "\
                                            "niveau,"\
                                            "experience,"\
                                            "force,"\
                                            "intelligence, "\
                                            "charisme, "\
                                            "dexterite, "\
                                            "constitution,"\
                                            "sagesse, "\
                                            "vie, "\
                                            "description,"\
                                            "classe_armure) "\
                        "VALUES "\
                        "(%(nom_entite)s,%(niveau)s,%(experience)s, %(force)s, %(intelligence)s, %(charisme)s, %(dexterite)s, %(constitution)s, %(sagesse)s,%(vie)s, %(description)s, %(classe_armure)s)"
   
                    , { "nom_entite" : entite.caracteristiques_entite.nom_entite
                    , "niveau": entite.caracteristiques_entite.niveau
                    , "experience": entite.caracteristiques_entite.experience
                    , "force": entite.caracteristiques_entite.force
                    , "intelligence": entite.caracteristiques_entite.intelligence
                    , "charisme": entite.caracteristiques_entite.charisme
                    , "dexterite": entite.caracteristiques_entite.dexterite
                    , "constitution": entite.caracteristiques_entite.constitution
                    , "sagesse": entite.caracteristiques_entite.sagesse
                    , "vie": entite.caracteristiques_entite.vie
                    , "description": entite.caracteristiques_entite.description
                    , "classe_armure": entite.caracteristiques_entite.classe_armure
                    }) 
            with DBConnection().connection as connection: # Nous récupérons l'id de l'entité.
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_entite) as max FROM Entite")
                    id_entite = cursor.fetchone()
                    id_ent = id_entite['max']
            entite.id_entite = id_ent
            EntiteDAO.ajouter_objets(entite)
            if hasattr(entite, "lore"):
                PersonnageDAO.add_personnage(entite)
            else:
                MonstreDAO.add_monstre(entite)
            UtilisateurEntiteDao.ajoute_utilisateur_entite(entite)

    @staticmethod    
    def ajouter_objets(entite: Entite): 
        for objet in entite.objets:
            with DBConnection().connection as connection: # Insertion de l'objet
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Objet (description_obj, "\
                                            "nom_objet) "\
                        "VALUES "\
                        "(%(description)s,%(nom)s)"
                    , { "description": objet.description_obj
                    , "nom": objet.nom_objet}) 
            with DBConnection().connection as connection: # Nous récupérons l'id de l'objet.
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT MAX(id_objet) as max FROM Objet")
                    id_obj = cursor.fetchone()
                    id_objet = id_obj['max']
            with DBConnection().connection as connection: # Nous complétons la table Entite_Objet.
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Entite_Objet (id_entite, "\
                                            "id_objet) "\
                        "VALUES "\
                        "(%(id_entite)s,%(id_objet)s)"
   
                    , { "id_entite" : entite.id_entite
                    , "id_objet": id_objet}) 
            
        
    @staticmethod    
    def get_entite_campagne(id_campagne):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT * FROM Entite WHERE id_campagne = %(id_campagne)s;"\
                    ,{"id_campagne": id_campagne}
                    )
                    entis = cursor.fetchall()
                    res = []
                    for dic in entis :
                        res.append(dic)
                return res
            
    @staticmethod    
    def get_entite(id_entite):
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT * FROM Entite WHERE id_entite = %(id_entite)s;"\
                    ,{"id_entite": id_entite}
                    )
                    entis = cursor.fetchall()
                    res = []
                    for dic in entis :
                        res.append(dic)
                return res
        
    @staticmethod
    def modifier_carac(id_entite,carac,valeur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Entite "\
                    "SET %(carac)s = %(valeur)s "\
                    "WHERE id_entite = %(id_entite)s;"\
                    , {"carac" : carac
                    , "valeur": valeur
                    , "id_entite": id_entite})
                
    @staticmethod
    def diminution_pv(nom_entite: str, nombre_pv): # Cette fonction n'est appelée que si l'entité a suffisamment de points de vies.
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT vie FROM Entite "\
                    "WHERE nom_entite = %(nom_entite)s;"\
                    , {"nom_entite": nom_entite}) 
                vie = cursor.fetchone()  
                vie = vie['vie']  
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Entite "\
                    "SET vie = %(vie)s"\
                    "WHERE nom_entite = %(nom_entite)s;"\
                    , {"vie" : vie - nombre_pv
                    , "nom_entite": nom_entite}) 

    @staticmethod
    def tuer(nom_entite: str): # Cette fonction réduit les points de vies des entités à 0.
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Entite "\
                    "SET vie = %(vie)s"\
                    "WHERE nom_entite = %(nom_entite)s;"\
                    , {"vie" : 0
                    , "nom_entite": nom_entite}) 
    
    @staticmethod
    def ajouter_entite_campagne(id_entite):
        id_camp = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Entite "\
                    "SET id_campagne = %(valeur)s "\
                    "WHERE id_entite = %(id_entite)s;"\
                    , { "valeur": id_camp
                    , "id_entite": id_entite})

    @staticmethod
    def existe_entite_campagne(id_entite): 
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (id_entite = %(id_entite)s)"\
                    , {"id_campagne" : id_campagne, "id_entite" : id_entite})
                res = cursor.fetchone()
        if res != None:
            return True
        else : 
            return False

    def entite_par_id(id_entite):
        from client.vue.session import Session
        id_campagne = Session.id_campagne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Entite "\
                    "WHERE (id_campagne = %(id_campagne)s) "\
                    "AND (Entite.id_entite = %(id_entite)s)"\
                    , {"id_campagne" : id_campagne, "id_entite" : id_entite})
                entite = cursor.fetchone()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Langage "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                langage = cursor.fetchall()
                if langage == None :
                    langage = []
                else :
                    langage = [langage[i]["nom_langage"] for i in range(len(langage))]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Capacite "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                capacite = cursor.fetchall()
                if capacite == None :
                    capacite = []
                else :
                    capacite = [capacite[i]["nom_capactite"] for i in range(len(capacite))]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "FROM Attaque "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                attaque = cursor.fetchall()
                if attaque == None:
                    attaque = []
                else :
                    attaque = [attaque[i]["nom_attaque"] for i in range(len(attaque))]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_objet "\
                    "FROM Entite_Objet "\
                    "WHERE id_entite = %(id_entite)s"\
                    , {"id_entite" : id_entite})
                objet = cursor.fetchall()
                if objet == None :
                    objet = []
                else : 
                    objet = [objet[i]["id_objet"] for i in range(len(langage))]
        liste_objet = []
        for id_objet in objet: 
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "\
                        "FROM Objet "\
                        "WHERE id_objet = %(id_objet)s"\
                        , {"id_objet" : id_objet})
                    obj = cursor.fetchone()
            liste_objet.append(Objet(id_objet = id_objet, nom_objet = obj["nom_objet"], description = obj["description"]))
        caract = Caracteristique(nom_entite = entite["nom_entite"], attaques = attaque, capacites = capacite, languages = langage, description = entite["description"], niveau = entite["niveau"], experience = entite["experience"], force = entite["force"], intelligence = entite["intelligence"], charisme = entite["charisme"], dexterite = entite["dexterite"], constitution = entite["constitution"], sagesse = entite["sagesse"], vie = entite["vie"], classe_armure = entite["classe_armure"])
        entite_id = Entite(id_joueur = -1, id_entite = id_entite, caracteristiques_entite = caract, objets = liste_objet)
        return entite_id
