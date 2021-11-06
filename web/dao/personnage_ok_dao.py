from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.personnage import Personnage
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

class PersonnageDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_personnage(perso : Personnage) -> Personnage:
            if perso.objets == None :
                personnage = Personnage(perso.classe, perso.race, perso.lore, perso.id_joueur, perso.id_entite, perso.nom_entite, perso.caracteristiques_entite, perso.objets)
            else:
                personnage = Personnage(perso.classe,perso.race,perso.lore,perso.id_joueur,perso.id_entite,perso.nom_entite,perso.caracteristiques_entite, perso.objets)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Personnage (id_entite, "\
                                                 "classe, "\
                                                 "race,"\
                                                 "lore) "\
                        "VALUES "\
                        "(%(id_entite)s, %(classe)s, %(race)s, %(lore)s)"\
   
                    , {"id_entite" : personnage.id_entite
                    , "classe" : personnage.classe
                    , "race": personnage.race
                    , "lore": personnage.lore
                    })
            
            return perso