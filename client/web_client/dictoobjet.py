
from client.web_client.trad_web import TradWebconfig
from objets_metier.caracteristique import Caracteristique

class DicToObjet():
    
    @staticmethod 
    def dictoobjet(dic,objet):
        dicobj = {}
        keys = objet.__dict__.keys()
        dictrad = TradWebconfig.trad(dic)
        for key in dictrad :
            if key in keys :
                dicobj.update({key : dictrad[key]})
        for key in keys : 
            if key not in dicobj : 
                dicobj.update({key : None})
        return(dicobj)
                
                
    @staticmethod
    def dictocarac(dico):
        dic = DicToObjet.dictoobjet(dico,Caracteristique('r'))
        return(Caracteristique(dic['nom_entite']
                             ,dic['attaques']
                             ,dic['capacites']
                             ,dic['languages']
                             ,dic['description']
                             ,dic['niveau']
                             ,dic['experience']
                             ,dic['force']
                             ,dic['intelligence']
                             ,dic['charisme']
                             ,dic['dexterite']
                             ,dic['constitution']
                             ,dic['sagesse']
                             ,dic['vie']
                             ,dic['classe_armure']
                             )) 
            
            
        
        