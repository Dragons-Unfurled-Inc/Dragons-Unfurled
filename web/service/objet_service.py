import requests as requ
from objets_metier.objet import Objet

from web.web_config import WebConfig

class ObjetService():
    
    def getListTypes():
        liste = WebConfig.getdnd('equipment-categories')
        listeTypes = []
        for dic in liste : 
            listeTypes.append(dic['index'])
            
    def getObjetsDeType(type) :
        url = str.format("{0}/{1}",'equipment-categories',type)
        objets = WebConfig.getdnd(url)  
        listeObjets = []
        for dic in objets['equipment']:
            listeObjets.append(dic['index'])
    
    def getTypeObjet(index):
        res = WebConfig.getdnd('magic-items')
        for dic in res['results'] : 
            if index == dic['index'] :
                return 'magic-items'
        return 'equipment'
            
    def getObjet(index):
        type = ObjetService.getTypeObjet(index)
        url = str.format("{0}/{1}",type,index)
        dicobjet = WebConfig.getdnd(url)
        desc = 'Pas de description'  
        if 'desc' in dicobjet.keys():
            desc = dicobjet['desc']
        return index,desc    
        
        

        