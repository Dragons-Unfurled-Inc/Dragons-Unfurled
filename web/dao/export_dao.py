import json
from pydantic.types import Json
from web.dao.db_connection import DBConnection




class ExportDAO():

    def sauvegarde_table(table):
        #fonction qui va dans une table et qui renvoie un json du contenu    
        query = str.format("select * from {}",table)
        cur = DBConnection().connection.cursor()
        cur.execute(query)
        r = []
        for row in cur.fetchall() :
                d = dict(row)
                if 'password' in d :
                    d.update({'password':str(d['password'],'utf8')})
                r.append(d)
        # cur.connection.close()
        return json.dumps(r)

    def sauvegarde_db():
        listetable = ExportDAO.liste_db()
        #fonction qui prend la liste de nom de tables et qui fait un dictionnaire avec les noms et les contenus
        dicdb = {}
        for nom in listetable :
            dicdb.update({nom : ExportDAO.sauvegarde_table(nom)})
        return dicdb

    def liste_db():
        #fonction qui renvoie une liste des noms de tables disponibles sur l'appareil
        cur2 = DBConnection().connection.cursor()
        cur2.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        listetable = []
        for table in cur2.fetchall():
            listetable.append(dict(table)['table_name'])
        return(listetable)