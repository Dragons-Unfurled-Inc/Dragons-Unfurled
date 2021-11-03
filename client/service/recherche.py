from typing import List

from utils.singleton import Singleton
from objets_metier.entite import Entite
# from objets_metier.feedback import Feedback
# from objets_metier.utilisateur import Utilisateur
# from web.dao.utilisateur_dao import UtilisateurDAO
# from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.entite_dao import EntiteDAO
from client.exceptions.entite_introuvable_exception import EntiteIntrouvableException


class Recherche(metaclass = Singleton):
    """
    Cette classe de recherche fait appel à nos DAO. 
    Elle permet de simplifier les requêtes en faisant appel aux bonnes DAO.
    """
    @staticmethod    
    def modifie_pv(self, entite: Entite, dommage: int):
        entite_nom = entite.caracteristiques_entite.nom_entite
        if entite_nom in EntiteDAO.liste_noms(): # Nous vérifions si cette entite existe dans notre base de données.
            if entite.caracteristiques_entite.vie > dommage:
                EntiteDAO.diminution_pv(entite_nom, dommage)
            else:
                EntiteDAO.tuer(entite_nom)
        else:
            raise EntiteIntrouvableException(entite_nom)