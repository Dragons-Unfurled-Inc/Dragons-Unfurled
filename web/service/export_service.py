

from web.dao.export_dao import ExportDAO


class ExportService():
    
    def SauvegardeTable(table):
        return ExportDAO.sauvegarde_table(table)
    
    def SauvegardeDB(listetable = []):
        return ExportDAO.sauvegarde_db(listetable)
    
    def ListeDB():
        return ExportDAO.liste_db()