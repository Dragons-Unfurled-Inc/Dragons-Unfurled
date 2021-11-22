from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

from objets_metier.entite import Entite  

class LangageDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_langage(enti : Entite) :
        if enti.objets == None : 
            entite = Entite(enti.id_joueur, enti.id_entite, enti.caracteristiques_entite)
        else:
            entite = Entite(enti.id_joueur, enti.id_entite, enti.caracteristiques_entite, enti.objets)
        for i in range(0, len(entite.caracteristiques_entite.languages)) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Langage (id_entite, "\
                                              "nom_langage) "\
                        "VALUES "\
                        "(%(id_entite)s,%(nom_langage)s)"\
   
                    , {"id_entite" : entite.id_entite
                    , "nom_langage" : entite.caracteristiques_entite.languages[i]
                    })