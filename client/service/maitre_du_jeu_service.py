from typing import List

from client.exceptions.utilisateur_introuvable_exception import \
    UtilisateurIntrouvableException
from objets_metier.feedback import FeedBack
from objets_metier.personnage import Personnage
from objets_metier.utilisateur import Utilisateur
from utils.singleton import Singleton
from web.dao.administrateur_dao import AdministrateurDAO
from web.dao.campagne_dao import CampagneDAO
from web.dao.donjon_dao import DonjonDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO
from web.dao.salle_dao import SalleDAO
from web.dao.utilisateur_dao import UtilisateurDAO


class MaitreDuJeuService(metaclass = Singleton):
  
    @staticmethod    
    def ajouter_entite_campagne(identifiant_entite): 
        EntiteDAO.ajouter_entite_campagne(identifiant_entite)

    @staticmethod    
    def retirer_entite_campagne(identifiant_entite): 
        EntiteDAO.retirer_entite_campagne(identifiant_entite) 

    @staticmethod    
    def existe_entite_nom_id_joueur(nom_entite, id_entite, id_joueur): 
        return MaitreDuJeuDAO.existe_entite_nom_id_joueur(nom_entite, id_entite, id_joueur)

    @staticmethod    
    def trouve_entite(identifiant_entite) -> Personnage: 
        pass

    @staticmethod
    def creer_campagne(nom_campagne: str): 
        CampagneDAO.creer_campagne(nom_campagne) 

    @staticmethod
    def voir_les_donjons():
        print("Voici l'ensemble des donjons, ainsi que leurs contenus :")
        donjons = MaitreDuJeuDAO.donjons()
        for donjon in donjons:
            print(donjon)
     
    @staticmethod
    def dict_entites():
        return MaitreDuJeuDAO.dict_entites()

    @staticmethod
    def dict_salles():
        return MaitreDuJeuDAO.dict_salles()

    @staticmethod
    def dict_monstres(id_campagne):
        return MaitreDuJeuDAO.dict_monstres(id_campagne)    

    @staticmethod
    def dict_personnages(id_campagne):
        return MaitreDuJeuDAO.dict_personnages(id_campagne)      

    @staticmethod
    def dict_pnj(id_campagne):
        return MaitreDuJeuDAO.dict_pnj(id_campagne)       

    @staticmethod
    def id_salle_contenant_entite(identifiant_entite):
        return SalleDAO.id_salle_contenant_entite(identifiant_entite) 
