from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite
from objets_metier.monstre import Monstre
from objets_metier.objet import Objet
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
        
    def getNetMonstre(nom):
        req = requ.get('https://www.dnd5eapi.co/api/monsters/' + nom)
        d=req.json()
        return (Monstre(d["type"],0,0,Caracteristique(d['name'],d['actions'],d['senses'],d['languages'],d['special_abilities']+d['legendary_actions'],'')))
    
    def getNetMonstreEtType():
        query = """query{
        monsters(limit : 500){name,type}
        }
        """
        endpoint="https://www.dnd5eapi.co/graphql"
        r = requ.post(endpoint,json={"query":query})
        noms_types = r.json()
        return(noms_types['data']['monsters'])
    
    def getNetMonstreParType():
        dicnom_type = MonstreService.getNetMonstreEtType()
        dic_types = {}
        for dic in dicnom_type : 
            if dic['type'] not in dic_types:
                 dic_types[dic['type']] = [dic['name']]
            else :
                dic_types.update({dic['type'] : dic_types[dic['type']]+[dic['name']]})
        return(dic_types)
    
    def getNetMonstreDeType(type):
        dic = MonstreService.getNetMonstreParType()
        return dic[type]
    
    @staticmethod
    def ImportListeTypes():
        return (MonstreService.getNetMonstreParType.keys())