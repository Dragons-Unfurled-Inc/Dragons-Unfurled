from web.dao.db_connection import DBConnection
from utils.singleton import Singleton
import requests as req
from abc import abstractstaticmethod

from objets_metier.entite import Entite  
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet

class AttaqueDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_attaque(enti : Entite) :
        for i in range(0, len((enti.caracteristiques_entite['attaques']))) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Capacité (nom_attaque, "\
                        "VALUES "\
                        "(%(nom_attaque)s)"\
   
                    , { "nom_attaque" : (enti.caracteristiques_entite)['attaques'][i]
                    })