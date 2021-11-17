from os import umask
from client.service.monstre_service import MonstreService
import requests as req
from objets_metier.joueur import Joueur
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.utilisateur import Utilisateur
from web.dao.campagne_dao import CampagneDAO
from pprint import pp, pprint
import hashlib
from web.dao.entite_dao import EntiteDAO
from web.dao.utilisateur_entite_dao import UtilisateurCampagneDao
from web.service.monstre_service import MonstreService
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
