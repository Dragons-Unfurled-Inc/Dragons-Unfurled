
from utils.singleton import Singleton
from objets_metier.entite import Entite
# from objets_metier.feedback import Feedback
# from objets_metier.utilisateur import Utilisateur
# from web.dao.utilisateur_dao import UtilisateurDAO
# from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.entite_dao import EntiteDAO
from client.exceptions.entite_introuvable_exception import EntiteIntrouvableException


class Recherche(metaclass = Singleton):


    @staticmethod    
    def modifie_pv(entite: Entite, dommage: int):
        id_entite = entite.id_entite
        if entite.caracteristiques_entite.vie > dommage:
            EntiteDAO.diminution_pv(id_entite, dommage)
        else:
            EntiteDAO.tuer(id_entite)