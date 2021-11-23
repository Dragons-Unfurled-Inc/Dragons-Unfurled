import hashlib
from os import umask
from pprint import pp, pprint
from googletrans import Translator

import requests as req
from dotenv import load_dotenv
from client.vue.session import Session

from client.web_client.dictoobjet import DicToObjet
from client.web_client.monstre_client import MonstreClient
from web.service.monstre_service import MonstreService
load_dotenv()
from objets_metier.caracteristique import Caracteristique
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage

#print(essai.__dict__())

#M = MonstreService.ImportMonstreWeb('aboleth')
#print(M)
def f():
    monstres = req.get('https://www.dnd5eapi.co/api/monsters')
    monstres = monstres.json()
    nom_monstres = [d["index"] for d in monstres["results"]]
    monstres_par_types = {}
    for monstre in nom_monstres : 
        dic_monstre = req.get('https://www.dnd5eapi.co/api/monsters/' + monstre)
        dic_monstre = dic_monstre.json()
        type_monstre = dic_monstre["type"]
        if type_monstre not in monstres_par_types:
            monstres_par_types[type_monstre] = [monstre]
        else :
            monstres_par_types.update({type_monstre : monstres_par_types[type_monstre]+[monstre]})
        print(monstres_par_types)
    print(monstres_par_types)

def h():
    caract = Caracteristique(nom_entite="Nom", attaques="Attaques", capacites="Capacité", languages="langages",description="des")
    perso = Personnage("classe","race","lore","id_joueur", "id_entite", "nomentite", caract)
    j = Joueur(personnages = [],choix_revelation = True,connecte = True,mot_de_passe = "bla",identifiant = "id",est_administrateur = True,feed_backs = True)
    j.personnages.append(perso)
    print(j.personnages)
'''connecte : bool,
                       mot_de_passe : str,
                       identifiant : str,
                       est_administrateur : bool, 
                       feed_backs : List[Feedback] = [],
                       choix_revelation : bool = True): '''
                       
def g():
    query = """query{
    monsters(limit:-1){name,type}
    }
    """
    endpoint="https://www.dnd5eapi.co/graphql"
    r = req.post("https://www.dnd5eapi.co/graphql",json={"query":query})
    print(r.status_code)
    names = r.json()
    print(names)

def t():
    c = Caracteristique(nom_entite = 'nom')
    #pprint(l)
    d = c.__dict__.keys()
    for key in d:
        print(key)

#print(UtilisateurCampagneDao.trouve_enti('Jules'))

def encode(mdp):
    pass_hash = mdp.encode()
    mdp = hashlib.sha256()
    mdp.update(pass_hash)
    print(mdp.digest())

#print(MonstreService.getNetMonstreDeType('humanoid'))
#print(MonstreService.ImportMonstreWeb('rat'))

# import os 
# print(os.environ['API_URL'])
# from web.dao.utilisateur_dao import UtilisateurDAO
# print(UtilisateurDAO.getUtilisateur('A'))

# from translate import Translator
# translator= Translator(to_lang="fr")
# translation = translator.translate("Strength")
# print(translation)
# translator = Translator()
# translator.detect('이 문장은 한글로 쓰여졌습니다.')
# translator.translate('yes', dest='fr')

# from deep_translator import GoogleTranslator
# translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig
# print(translated)

# monstres = req.get('https://www.dnd5eapi.co/api/monsters/aboleth')
# monstres = monstres.json()
# print(monstres.keys())

# dic = DicToObjet.dictoobjet({'index': 'aboleth', 'name': 'Aboleth', 'size': 'Large', 'type': 'aberration', 'subtype': None, 'alignment': 'lawful evil', 'armor_class': 17, 'hit_points': 135, 'hit_dice': '18d10', 'speed': {'walk': '10 ft.', 'swim': '40 ft.'}, 'strength': 21, 'dexterity': 9, 'constitution': 15, 'intelligence': 18, 'wisdom': 15, 'charisma': 18, 'proficiencies': [{'proficiency': {'index': 'saving-throw-con', 'name': 'Saving Throw: CON', 'url': '/api/proficiencies/saving-throw-con'}, 'value': 6}, {'proficiency': {'index': 'saving-throw-int', 'name': 'Saving Throw: INT', 'url': '/api/proficiencies/saving-throw-int'}, 'value': 8}, {'proficiency': {'index': 'saving-throw-wis', 'name': 'Saving Throw: WIS', 'url': '/api/proficiencies/saving-throw-wis'}, 'value': 6}, {'proficiency': {'index': 'skill-history', 'name': 'Skill: History', 'url': '/api/proficiencies/skill-history'}, 'value': 12}, {'proficiency': {'index': 'skill-perception', 'name': 'Skill: Perception', 'url': '/api/proficiencies/skill-perception'}, 'value': 10}], 'damage_vulnerabilities': [], 'damage_resistances': [], 'damage_immunities': [], 'condition_immunities': [], 'senses': {'darkvision': '120 ft.', 'passive_perception': 20}, 'languages': 'Deep Speech, telepathy 120 ft.', 'challenge_rating': 10, 'xp': 5900},Caracteristique(nom_entite= 'test'))
# print(dic)
# carac = Caracteristique(nom_entite = 't')
# print(getattr(carac,'force'))
#print(Caracteristique().parse_obj(dic))
# carac = Caracteristique('nom')
# m=Monstre("type",'id_joueur','id_entite',carac)
# print(m) 

# Session.utilisateur = Joueur(identifiant = 'jules')
# print(MonstreClient.ImportMonstreWeb('aboleth'))

print(MonstreService.getNetAttaquesMonstre('Adult Blue Dragon','Bite'))