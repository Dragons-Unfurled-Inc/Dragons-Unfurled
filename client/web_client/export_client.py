
from client.vue.session import Session
from client.web_client.trad_web import TradWebconfig


class ExportClient():
    
    
    def SauvegardeTable(table : str):
        configuration = TradWebconfig()
        url = str.format('table/{}',table)
        d = configuration.getTrad(url)
        return d
            
    def SauvegardeDB():
        configuration = TradWebconfig()
        d = configuration.getTrad('tables/contenu')
        return d
    
    