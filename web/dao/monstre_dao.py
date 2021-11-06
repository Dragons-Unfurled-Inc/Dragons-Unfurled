from objets_metier.objet import Objet
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.caracteristique import Caracteristique
from objets_metier.monstre import Monstre

class MonstreDAO(metaclass = Singleton):
    
    @staticmethod    
    def add_personnage(monstre : Monstre) -> Monstre:
            if monstre.objets == None :
                monstre = Monstre(monstre.type, monstre.id_joueur, monstre.id_entite, Caracteristique.parse_obj(monstre.caracteristiques_entite))
            else:
                monstre = Monstre(monstre.type, monstre.id_joueur, monstre.id_entite, Caracteristique.parse_obj(monstre.caracteristiques_entite), Objet.parse_obj(monstre.objets))
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Monstre (type) "\
                        "VALUES "\
                        "(%(type)s)"\
   
                    , {"type" : monstre.type
                    })
            
            return monstre