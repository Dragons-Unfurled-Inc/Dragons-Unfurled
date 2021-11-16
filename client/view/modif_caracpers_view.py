from client.view.abstract_view import AbstractView
from PyInquirer import prompt
from view.session import Session
from objets_metier.caracteristique import Caracteristique
from web.dao.entite_dao import EntiteDAO
from web.dao.maitre_du_jeu_dao import MjDAO
from web.dao.utilisateur_entite_dao import UtilisateurCampagneDao

class ModifCaracView(AbstractView):

    def __init__(self):
        utilisateur = Session.utilisateur
        id_campagne = utilisateur.id_campagne
        id_entis = UtilisateurCampagneDao.trouve_enti(utilisateur.identifiant)
        entis_camp = EntiteDAO.get_entite_campagne(id_campagne)
        for id in id_entis : 
            for enti in entis_camp :
                if enti.id_entite == id :
                    enti_perso = enti
                    self.id_enti = id 
        #matcher l'id entre entis et entis_camp et hop on a l'entite du joueur, ensuite faire modif enti.caracs en choixx
        self.list_choix = enti_perso.caracteristiques_entite.__dict__.keys() 
        self.questions = [
                {
                    'type': 'list',
                    'name': 'Nom',
                    'message': 'Que souhaitez-vous modifier ?',
                    'choices' : self.list_choix 
                },
                {
                    'type': 'input',
                    'name': 'Val',
                    'message': 'Quelle est la nouvelle valeur ?'
                }
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.questions)
        EntiteDAO.modifier_carac(self.id_enti,reponse['Nom'],reponse['Val'])