from translate import Translator      
  
class Trad():
    
        @staticmethod
        def trad(dic,language = "fr"):
        translator= Translator(to_lang=language)
        dictraduit = {}
        for key in dic :
            keytrad = translator.translate(key)
            dictrad = translator.translate(dic['key'])
            dictraduit.update{keytrad : dictrad}
            
        translation = translator.translate("Strength")