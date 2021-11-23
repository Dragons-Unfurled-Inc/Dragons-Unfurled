from client.web_client.dictoobjet import DicToObjet
from objets_metier.caracteristique import Caracteristique


class CaracClient():
    
    @staticmethod
    def dictocarac(dic):
        DicToObjet.dictoobjet(dic,Caracteristique('r'))
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