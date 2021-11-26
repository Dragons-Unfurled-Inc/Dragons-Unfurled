from web.dao.db_connection import DBConnection

from utils.singleton import Singleton

from objets_metier.entite import Entite  

class AttaqueDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_attaque(enti : Entite) :
        if enti.objets == None : 
            entite = Entite(enti.id_joueur, enti.id_entite, enti.caracteristiques_entite)
        else:
            entite = Entite(enti.id_joueur, enti.id_entite, enti.caracteristiques_entite, enti.objets)
        for i in range(0, len((entite.caracteristiques_entite.attaques))) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Attaque (id_entite, "\
                                              "nom_attaque) "\
                        "VALUES "\
                        "(%(id_entite)s, %(nom_attaque)s)"\
   
                    , { "id_entite" : entite.id_entite
                    , "nom_attaque" : entite.caracteristiques_entite.attaques[i]
                    })
                    
    def ajout_attaque(id_entite,attaques):
        for i in range(0, len(attaques)) :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Attaque (id_entite, "\
                                              "nom_attaque) "\
                        "VALUES "\
                        "(%(id_entite)s, %(nom_attaque)s)"\
   
                    , { "id_entite" : id_entite
                    , "nom_attaque" : attaques[i]
                    })