from objets_metier.caracteristique import Caracteristique
from objets_metier.personnage import Personnage
from objets_metier.objet import Objet
from objets_metier.utilisateur import Utilisateur
from web.dao.db_connection import DBConnection
from client.exceptions.utilisateur_introuvable_exception import UtilisateurIntrouvableException


class MjDAO:

    # @staticmethod
    # def personnages_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso joueurs 
    #     with DBConnection().connection as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute(
    #                 "SELECT classe, race, lore, id_joueur, id_entite, nom_entite, force, experience, intelligence, charisme, dexterite, constitution, description, sagesse, vie, nom_attaque, nom_capacite, nom_langage, description_obj "\
    #                 "FROM Entite "\
    #                 "JOIN Personnage ON Personnage.id_entite = Entite.id_entite"\
    #                 "JOIN Capacite ON Entite.id_entite = Capacite.id_entite"\
    #                 "JOIN Langage ON Entite.id_entite = Langage.id_entite"\
    #                 "JOIN Attaque ON Entite.id_entite = Attaque.id_entite"\
    #                 "JOIN Entite_Objet ON Entite.id_entite = Entite_Objet.id_entite"\
    #                 "JOIN Objet ON Entite_Objet.id_objet = Objet.id_Objet"
    #                 "WHERE id_campagne = %(id_campagne)s;"\
    #                 , {"id_campagne" : id_campagne})
    #             perso = cursor.fetchone()
    #             nom_entite = [perso["id_entite"],perso["nom_entite"]]
    #             force = [perso["id_entite"],perso["force"]]
    #             experience = [perso["id_entite"],perso["experience"]]
    #             intelligence = [perso["id_entite"],perso["intelligence"]]
    #             charisme = [perso["id_entite"],perso["charisme"]]
    #             dexterite = [perso["id_entite"],perso["dexterite"]]
    #             constitution = [perso["id_entite"],perso["constitution"]]
    #             vie = [perso["id_entite"],perso["vie"]]
    #             sagesse = [perso["id_entite"],perso["sagesse"]]
    #             attaques = [perso["id_entite"],perso["nom_attaque"]]
    #             langages = [perso["id_entite"],perso["nom_langage"]]
    #             objet = [perso["id_entite"], perso["nom_objet"], perso["description_obj"]]
    #             capacites = [perso["id_entite"],perso["nom_capacite"]]
    #             enti_description = [perso["id_entite"],perso["description"]]
    #             classe_armure = [perso["id_entite"],perso["classe_armure"]]
    #             classe = [perso["id_entite"],perso["classe"]]
    #             race = [perso["id_entite"],perso["race"]]
    #             lore = [perso["id_entite"],perso["lore"]]
    #             id_entite = perso["id_entite"]
    #             id_joueur = [perso["id_entite"],perso["id_joueur"]]
    #             description = [perso["id_entite"],perso["description"]]    
    #     liste_perso = []       
    #     for i in range(0, max(id_entite)):
    #         cur = 0 
    #         liste_attaques = []
    #         while attaques[0][cur] == i :
    #             liste_attaques.append(attaques[1][cur])
    #             cur += 1
    #         cur = 0
    #         liste_langages = []
    #         while langages[0][cur] == i :
    #             liste_langages.append(langages[0][cur])
    #             cur += 1
    #         cur = 0 
    #         liste_capacites = []
    #         while capacites[0][cur] == i:
    #             liste_capacites.append(capacites[1][cur])
    #             cur+=1
    #         carac = Caracteristique(nom_entite = nom_entite, force = force, experience = experience, intelligence = intelligence, charisme = charisme, dexterite = dexterite, constitution = constitution, vie = vie, sagesse =  sagesse, attaques= liste_attaques, capacites = liste_capacites, languages = liste_langages, description = enti_description, classe_armure = classe_armure)
    #         cur = 0
    #         liste_objet = []
    #         while objet[0][cur] == i: 
    #             None
    #         liste_perso.append(Personnage(classe, race, lore, id_joueur, id_entite, nom_entite, carac, liste_objet))
    #     return liste_perso
#A finir 
    
    @staticmethod
    def personnages_joueurs(id_campagne): 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_entite "\
                    "FROM Entite "\
                    "WHERE id_campagne = %(id_campagne)s"\
                    , {"id_campagne" : id_campagne})
                liste_entite = cursor.fetchone()
                liste_entite = liste_entite["id_entite"]
        liste_perso = []
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
            liste_perso.append(Personnage(entite["classe"], entite["race"], entite["lore"],entite["id_joueur"], i, entite["nom_entite"], caract, liste_objet))
        return liste_perso
                
    @staticmethod
    def personnages_non_joueurs(id_campagne): # Cette fonction renvoie l'ensemble des perso non joueurs 
        return []

    @staticmethod
    def monstres(id_campagne):# Cette fonction renvoie l'ensemble des pmonstres 
        return []

    @staticmethod
    def donjons(id_campagne):# Cette fonction renvoie l'ensemble des donjons
        return []            
