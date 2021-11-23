import requests as requ
from client.vue.session import Session
from client.web_client.dictoobjet import DicToObjet
from client.web_client.trad_web import TradWebconfig
from client.web_client.web_configuration import WebConfiguration
from objets_metier.caracteristique import Caracteristique
from objets_metier.joueur import Joueur
from objets_metier.monstre import Monstre
from web.dao.monstre_dao import MonstreDAO

class MonstreClient():
    
        @staticmethod
        def ImportMonstreWeb(nom = str):
            Session.utilisateur = Joueur(identifiant = 'jules')
            util = Session.utilisateur
            configuration = TradWebconfig()
            d = configuration.getTrad('monstre/' + nom)
            carac = DicToObjet.dictocarac(d)
            return Monstre(util.identifiant,-1,d['type'],carac)
            
    
        @staticmethod
        def ImportMonstreParType(triche = bool):
            pass
        
        @staticmethod
        def ImportListeTypes():
            pass
            