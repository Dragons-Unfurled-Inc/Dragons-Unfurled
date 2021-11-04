from web.dao.db_connection import DBConnection
from utils.singleton import Singleton
import requests as req
from abc import abstractstaticmethod

from objets_metier.entite import Entite  
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet

class LangageDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_langage(enti : Entite) :
        for i in range(0, len(enti.caracteristiques_entite.__languages)) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Capacité (id_entite, "\
                                               "nom_langage, "\
                        "VALUES "\
                        "(%(id_entite)s,%(nom_langage)s)"\
   
                    , { "id_entite" : enti.id_entite
                    , "nom_langage" : enti.caracteristiques_entite.__languages[i]
                    })