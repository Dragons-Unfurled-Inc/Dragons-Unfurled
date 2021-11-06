from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.personnage import Personnage
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

class PersonnageDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_personnage(perso : Personnage) -> Personnage:
            if perso.objets == None :
                personnage = Personnage(perso.classe,perso.race,perso.lore,perso.id_joueur,perso.id_entite,perso.nom_entite,Caracteristique.parse_obj(perso.caracteristiques_entite))
            else:
                personnage = Personnage(perso.classe,perso.race,perso.lore,perso.id_joueur,perso.id_entite,perso.nom_entite,Caracteristique.parse_obj(perso.caracteristiques_entite), Objet.parse_obj(perso.objets))
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Personnage (classe, "\
                                                 "race,"\
                                                 "lore) "\
                        "VALUES "\
                        "( %(classe)s, %(race)s, %(lore)s)"\
   
                    , {"classe" : personnage.classe
                    , "race": personnage.race
                    , "lore": personnage.lore
                    })
            
            return personnage