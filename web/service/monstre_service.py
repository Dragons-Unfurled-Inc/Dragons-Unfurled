from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
from objets_metier.monstre import Monstre
from web.dao.entite_dao import EntiteDAO
from web.dao.monstre_dao import MonstreDAO
from web.dao.attaque_dao import AttaqueDAO
from web.dao.capacite_dao import CapaciteDAO
from web.dao.langage_dao import LangageDAO
from web.dao.entite_objet_dao import ObjetEntiteDAO
import requests as requ

class MonstreService():
    @staticmethod
    def add_monstre(monstre : Monstre):
        entite = Entite(monstre.id_joueur, monstre.id_entite, monstre.caracteristiques_entite,monstre.objets)
        entite_persistee = EntiteDAO.add_entite(entite)
        AttaqueDAO.add_attaque(entite_persistee)
        CapaciteDAO.add_capacite(entite_persistee)
        LangageDAO.add_langage(entite_persistee)
        monstre = Monstre(monstre.type, monstre.id_joueur, entite_persistee.id_entite, monstre.caracteristiques_entite, monstre.objets)
        if monstre.objets != None: 
            ObjetEntiteDAO.add_entite_objet(entite_persistee)
        MonstreDAO.add_personnage(monstre)
    
    @staticmethod  
    def getNetMonstre(nom):
        req = requ.get('https://www.dnd5eapi.co/api/monsters/' + nom)
        return req.json()
    
    @staticmethod
    def getNetMonstreEtType():
        query = """query{
        monsters(limit : 500){name,type}
        }
        """
        endpoint="https://www.dnd5eapi.co/graphql"
        r = requ.post(endpoint,json={"query":query})
        noms_types = r.json()
        return(noms_types['data']['monsters'])
    
    @staticmethod
    def getNetMonstreParType():
        dicnom_type = MonstreService.getNetMonstreEtType()
        dic_types = {}
        for dic in dicnom_type : 
            if dic['type'] not in dic_types:
                 dic_types[dic['type']] = [dic['name']]
            else :
                dic_types.update({dic['type'] : dic_types[dic['type']]+[dic['name']]})
        return(dic_types)
    
    @staticmethod
    def getNetMonstreDeType(type):
        dic = MonstreService.getNetMonstreParType()
        return dic[type]
    
    @staticmethod
    def ImportListeTypes():
        return (MonstreService.getNetMonstreParType.keys())
    
    @staticmethod
    def getNetAttaquesMonstre(monstre,attaque):
        query = """query{
monsters(limit:-1){name,actions{name,desc,damage{damage_dice,damage_type{name}},attack_bonus}, legendary_actions{name,desc,attack_bonus}}
}
        """
        endpoint="https://www.dnd5eapi.co/graphql"
        r = requ.post(endpoint,json={"query":query})
        noms_attaques = r.json()
        dic = noms_attaques['data']['monsters']
        for mon in dic : 
            if mon['name'] == monstre :
                for attack in mon['actions'] : 
                    if attack['name'] == attaque : 
                        return(attack)
        