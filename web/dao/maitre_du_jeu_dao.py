from objets_metier.caracteristique import Caracteristique
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
                    "SELECT classe, race, lore, id_joueur, id_entite, nom_entite, force, experience, intelligence, charisme, dexterite, constitution, sagesse, vie, nom_attaque, nom_capacite, nom_langage "\
                    "FROM Entite "\
                    "JOIN Personnage ON Personnage.id_entite = Entite.id_entite"\
                    "JOIN Capacite ON Entite.id_entite = Capacite.id_entite"\
                    "JOIN Langage ON Entite.id_entite = Langage.id_entite"\
                    "JOIN Attaque ON Entite.id_entite = Attaque.id_entite"\
                    "JOIN Entite_Objet ON Entite.id_entite = Entite_Objet.id_entite"\
                    "JOIN Objet ON Entite_Objet.id_objet = Objet.id_Objet"
                    "WHERE id_campagne = %(id_campagne)s;"\
                    , {"id_campagne" : id_campagne})
                perso = cursor.fetchone()
                nom_entite = [perso["id_entite"],perso["nom_entite"]]
                force = [perso["id_entite"],perso["force"]]
                experience = [perso["id_entite"],perso["experience"]]
                intelligence = [perso["id_entite"],perso["intelligence"]]
                charisme = [perso["id_entite"],perso["charisme"]]
                dexterite = [perso["id_entite"],perso["dexterite"]]
                constitution = [perso["id_entite"],perso["constitution"]]
                vie = [perso["id_entite"],perso["vie"]]
                sagesse = [perso["id_entite"],perso["sagesse"]]
                
                
                
                enti_description = [perso["id_entite"],perso["description"]]
                classe_armure = [perso["id_entite"],perso["classe_armure"]]
                classe = [perso["id_entite"],perso["classe"]]
                race = [perso["id_entite"],perso["race"]]
                lore = [perso["id_entite"],perso["lore"]]
                id_entite = perso["id_entite"]
                id_joueur = [perso["id_entite"],perso["id_joueur"]]
                description = [perso["id_entite"],perso["description"]]             
        liste_perso = []
        for i in range(0, len(perso["username"])):
            carac = Caracteristique(nom_entite = nom_entite, force = force, experience = experience, intelligence = intelligence, charisme = charisme, dexterite = dexterite, constitution = constitution, vie = vie, sagesse =  sagesse, attaques= attaques, capacites = capacites, languages = languages, description = description, classe_armure = classe_armure)
            liste_perso.append(Personnage(classe, race, lore, id_joueur, id_entite, nom_entite, carac, objet))
        return liste_perso
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
