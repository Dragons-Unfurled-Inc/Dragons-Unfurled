
from web.dao.administrateur_dao import AdministrateurDAO


class AdministrateurService:
    """
    Cette classe fournit les services permettant de gérer le transfert des droits administrateur.
    """

    @staticmethod
    def supprimer_droits_administrateur(nom_administrateur_donneur: str):
        AdministrateurDAO.supprimer_droits_administrateur(nom_administrateur_donneur)

    @staticmethod
    def ajouter_droits_administrateur(nom_administrateur_donneur: str):
        AdministrateurDAO.ajouter_droits_administrateur(nom_administrateur_donneur)

    @staticmethod
    def supprimer_compte(nom_utilisateur: str):
        AdministrateurDAO.supprimer_compte(nom_utilisateur)
        