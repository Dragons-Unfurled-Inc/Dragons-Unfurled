from web.dao.db_connection import DBConnection


class CombatDAO : 

    @staticmethod
    def add_combat(id_jet : int , id_enti1 : int, id_enti2: int):
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO Combat (id_jet, "\
                                         "id_entite1, "\
                                         "id_entite2)"\
                        "VALUES "\
                        "(%(id_jet)s,%(id_entite1)s,%(id_entite2)s)"\
   
                    , {"id_jet" : id_jet
                    , "id_entite1" : id_enti1
                    , "id_entite2" : id_enti2
                    })