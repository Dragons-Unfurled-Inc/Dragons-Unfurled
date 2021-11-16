from client.view.abstract_view import AbstractView
from PyInquirer import prompt
from view.session import Session
from objets_metier.caracteristique import Caracteristique
from web.dao.entite_dao import EntiteDAO
from web.dao.maitre_du_jeu_dao import MjDAO
from web.dao.utilisateur_entite_dao import UtilisateurCampagneDao

class ModifPersView(AbstractView):
    def __init__(self):
        utilisateur = Session.utilisateur
        campagne = utilisateur.id_campagne
        entis = UtilisateurCampagneDao.trouve_enti(utilisateur.identifiant)
        entis_camp = EntiteDAO.get_entite(campagne)
        #matcher l'id entre entis et entis_camp et hop on a l'entite du joueur, ensuite faire modif enti.caracs en choixx
        self.list_choix = 
        def f():
            return 't'
        self.questions = [
                {
                    'type': 'list',
                    'name': 'Nom',
                    'message': 'Que souhaitez-vous modifier ?',
                    'choices' :  d = c.__dict__.keys()
                                    for key in d:
                                        print(key)
                },
                {
                    'type': 'input',
                    'name': 'Nom',
                    'message': 'Que souhaitez-vous modifier ?',
                    'choices' : ModifPersView.f()
                    'filter' lambda val: int(val)
                }  
            ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
            
    def make_choice(self):
        reponse = prompt(self.questions)