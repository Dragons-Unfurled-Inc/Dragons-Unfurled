
from client.vue.session import Session
from client.web_client.trad_web import TradWebconfig


class ExportClient():
    
    
    def SauvegardeTable(table : str):
        configuration = TradWebconfig()
        url = str.format('table/',table)
        d = configuration.getTrad(url)
        return stock(d.json())
            
    def SauvegardeDB():
        configuration = TradWebconfig()
        d = configuration.getTrad('table/contenu')
        return stock(d.json())
    
    def ListeDB():
        configuration = TradWebconfig()
        d = configuration.getTrad('tables/liste/')
        return d
