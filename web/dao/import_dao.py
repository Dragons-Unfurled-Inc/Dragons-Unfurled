from objets_metier.entite import Entite
from web.dao.attaque_dao import AttaqueDAO
from web.dao.campagne_dao import CampagneDAO
from web.dao.capacite_dao import CapaciteDAO
from web.dao.cellule_dao import CelluleDAO
from web.dao.combat_dao import CombatDAO
from web.dao.db_connection import DBConnection
from web.dao.donjon_dao import DonjonDAO
from web.dao.entite_dao import EntiteDAO
from web.dao.entite_objet_dao import ObjetEntiteDAO
from web.dao.feed_back_dao import FeedBackDAO
from web.dao.jet_dao import JetDAO
from web.dao.langage_dao import LangageDAO
from web.dao.objet_dao import ObjetDAO
from web.dao.utilisateur_campagne_dao import UtilisateurCampagneDao
from web.dao.utilisateur_dao import UtilisateurDAO
from web.dao.utilisateur_entite_dao import UtilisateurEntiteDao
class ImportDAO():
    
    @staticmethod
    def strversfonction(str):
        #fonction qui prend les noms de tables et qui renvoie les DAO à utiliser pour importer
        #pas assez de temps à ce jour, nos DAO prennent des objets en argument et ce n'est pas le plus pratique
        dic = {'personnages' : [EntiteDAO.ajoute_entite, Entite]
            ,'campagne' : CampagneDAO.creer_campagne
            ,'donjon' : DonjonDAO.ajoute_donjon
            ,'cellule' : CelluleDAO.add_cellule
            ,'entite' : EntiteDAO.ajoute_entite
            ,'capacite' : CapaciteDAO.ajout_capacite
            ,'langage' : LangageDAO.ajout_language
            ,'attaque' : AttaqueDAO.ajout_attaque
            ,'personnage' : EntiteDAO.ajoute_entite
            ,'monstre' : EntiteDAO.ajoute_entite
            ,'jet' : JetDAO.ajout_jet
            ,'objet' : ObjetDAO.ajouter_objet
            ,'combat' : CombatDAO.add_combat
            ,'utilisateur' : UtilisateurDAO.createUtilisateur
            ,'feedback' : FeedBackDAO.donner_feedback
            ,'utilisateur_entite' : UtilisateurEntiteDao.importe_utilisateur_entite
            ,'utilisateur_campagne' : UtilisateurCampagneDao.add_utilisateur_campagne
            ,'entite_objet': ObjetEntiteDAO.import_entite_objet
            }
        return dic[str]