from objets_metier.monstre import Monstre
from utils.singleton import Singleton
from web.dao.db_connection import DBConnection


class MonstreDAO(metaclass = Singleton):
    
    @staticmethod    
    def add_monstre(monstre : Monstre) -> Monstre:
            # if monstre.objets == None :
            #     mons = Monstre(monstre.type, monstre.id_joueur, monstre.id_entite, monstre.caracteristiques_entite)
            # else:
            #     mons = Monstre(monstre.type, monstre.id_joueur, monstre.id_entite, monstre.caracteristiques_entite, monstre.objets)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Monstre (id_entite, "\
                                             "type) "\
                        "VALUES" \
                        "(%(id_entite)s, %(type)s)"\
   
                    , { "id_entite" : monstre.id_entite
                    , "type" : monstre.type
                    })
