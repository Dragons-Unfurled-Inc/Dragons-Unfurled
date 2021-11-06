from web.dao.db_connection import DBConnection
from utils.singleton import Singleton
import requests as req
from abc import abstractstaticmethod

from objets_metier.entite import Entite  
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet

class CapaciteDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_capacite(enti : Entite) :
        if enti.objets == None : 
            entite = Entite(enti.id_joueur, enti.id_entite, Caracteristique.parse_obj(enti.caracteristiques_entite))
        else:
            entite = Entite(enti.id_joueur, enti.id_entite, Caracteristique.parse_obj(enti.caracteristiques_entite), Objet.parse_obj(enti.objets))
        for i in range(0, len(entite.caracteristiques_entite.capacites)) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Capacite (nom_capacite)"\
                        "VALUES "\
                        "(%(nom_capacite)s)"\
   
                    , { "nom_capacite" : entite.caracteristiques_entite.capacites[i]
                    })