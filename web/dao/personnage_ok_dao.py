from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
from objets_metier.personnage import Personnage
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

class PersonnageDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_personnage(personnage : Personnage) -> Personnage:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Personnage (classe, "\
                                                 "race,"\
                                                 "lore) "\
                        "VALUES "\
                        "(%(classe)s, %(race)s, %(lore)s)"\
   
                    , {"classe" : personnage.classe
                    , "race": personnage.race
                    , "lore": personnage.lore
                    })
            
            return personnage