from client.web_client.web_configuration import WebConfiguration
from googletrans import Translator


class TradWebconfig(WebConfiguration):
    
    @staticmethod
    def trad(dic):
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
                , 'actions' : 'attaques'
                , 'legendary_actions' : 'attaques_legendaires'}
        if (mot in dic.keys()) : 
            return (dic[mot])
        return mot
        
            