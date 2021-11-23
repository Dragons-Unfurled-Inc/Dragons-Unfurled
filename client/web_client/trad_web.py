from googletrans import Translator
from client.web_client.web_configuration import WebConfiguration  

class TradWebconfig(WebConfiguration):
    
    @staticmethod
    def trad2(dic,language = "fr"):
        translator = Translator(service_urls='translate.google.com')
        dictraduit = {}
        for key in dic :
            keytrad = translator.translate(key, dest=language)
            dictrad = {}
            if isinstance(dic[key], dict):
                dictrad = TradWebconfig.trad(dic[key])
            if (dic[key] == None):
                dictrad= "absent"
            if isinstance(dic[key], int):
                dictrad = dic[key]
            if isinstance(dic[key],list):
                listetrad = []
                for elem in dic[key] :
                    listetrad.append(TradWebconfig.trad(elem))
                dictrad = listetrad
            if isinstance(dic[key],str):
                dictrad = translator.translate(dic[key], dest=language)
            dictraduit.update({keytrad : dictrad})
        print(dictraduit)
        return dictraduit
    
    @staticmethod
    def trad(dic,language = "fr"):
        dictraduit = {}
        for key in dic :
            keytrad = TradWebconfig.libtrad(key)
            dictraduit.update({keytrad : dic[key]})
        return dictraduit
    
    def getTrad(self,req:str):
        request = super().get(req)
        return TradWebconfig.trad(request)
    
    @staticmethod
    def libtrad(mot):
        dic = {'name' : 'nom_entite'
                , 'size' : 'taille'
                , 'type' : 'type'
                , 'armor_class' : 'classe_armure'
                , 'hit_points' : 'vie'
                , 'strength' : 'force'
                , 'dexterity' : 'dexterite'
                , 'wisdom' : 'sagesse'
                , 'charisma' : 'charisme'
                , 'actions' : 'attaques'
                , 'desc' : 'description'
                , 'xp' : 'experience'
                , 'level' : 'niveau'
                , 'special_abilities' : 'capacites'
                , 'challenge_rating' : 'niveau'
                , 'actions' : 'attaques'}
        if (mot in dic.keys()) : 
            return (dic[mot])
        return mot
        
            