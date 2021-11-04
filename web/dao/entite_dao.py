from web.dao.db_connection import DBConnection
from utils.singleton import Singleton
import requests as req
from abc import abstractstaticmethod

from objets_metier.entite import Entite  
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet

#le code est pas ouf mais vous avez une idée de comment faire, par contre c'est ptet plus à sa place dans le package web
class EntiteDAO:
    # @staticmethod
    # def creation_monstre(nom): 
    #     r = req.get('https://www.dnd5eapi.co/api/monsters/aboleth') 
    #     d=r.json()
    #     return(Monstre(nom,d["size"],d["alignment"],d['armor_class'],d['hit_points'],d['hit_dice'],d['speed'],d['strength'],d['dexterity'],d['constitution'],d['intelligence'],d['wisdom'],d['charisma'],d['proficiencies'],d['languages'],d['xp'])) 

    @staticmethod    
    def add_entite(enti : Entite) -> Entite:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    caract = Caracteristique(nom_entite="Nom", attaques="Attaques", capacites="Capacité", languages="langages",description="des")
                    obj = Objet("id_objet", "nom_objet","des")
                    enti = Entite("id joueur","id entite",caract, [obj])
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
   
                    , { "nom_entite" : enti.caracteristiques_entite.nom_entite
                    , "niveau": enti.caracteristiques_entite.niveau
                    , "experience": enti.caracteristiques_entite.experience
                    , "force": enti.caracteristiques_entite.force
                    , "intelligence": enti.caracteristiques_entite.intelligence
                    , "charisme": enti.caracteristiques_entite.charisme
                    , "dexterite": enti.caracteristiques_entite.dexterite
                    , "constitution": enti.caracteristiques_entite.constitution
                    , "sagesse": enti.caracteristiques_entite.sagesse
                    , "vie": enti.caracteristiques_entite.vie
                    , "description": enti.caracteristiques_entite.description
                    , "classe_armure": enti.caracteristiques_entite.classe_armure
                    }) 
            return enti
            
    @staticmethod
    def diminution_pv(nom_entite: str): # Cette fonction n'est appelée que si l'entité a suffisamment de points de vies.
        return 

    @staticmethod
    def tuer(nom_entite: str): # Cette fonction réduit les points de vies des entités à 0.
        return 
