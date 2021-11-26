from web.dao.campagne_dao import CampagneDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.maitre_du_jeu_dao import MaitreDuJeuDAO
from web.dao.salle_dao import SalleDAO

from objets_metier.personnage import Personnage

from utils.singleton import Singleton


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
    def dict_objets():
        return MaitreDuJeuDAO.dict_objets()

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

    @staticmethod
    def id_salle_contenant_objet(identifiant_objet):
        return SalleDAO.id_salle_contenant_objet(identifiant_objet) 

    @staticmethod
    def retirer_objet_salle(id_objet: int):
        return MaitreDuJeuDAO.retirer_objet_salle(id_objet)

    @staticmethod
    def retirer_entite_salle(id_entite: int):
        return MaitreDuJeuDAO.retirer_entite_salle(id_entite)
