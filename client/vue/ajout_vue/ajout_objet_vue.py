from client.service.donjon_service import DonjonService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.monstre_service import MonstreService
from client.service.objet_service import ObjetService
from client.vue.abstract_vue import AbstractVue

from web.dao.entite_dao import EntiteDAO

from objets_metier.entite import Entite

from PyInquirer import prompt



class AjoutObjVue(AbstractVue):
    
    @staticmethod
    def choix(reponse): 
        return ObjetService.ImportObjetDeType(reponse['type'])
    
    def __init__(self):
        self.liste_types = ObjetService.ImportListeTypes()
        self.questions = [
            {
                'type': 'list',
                'name': 'type',
                'message': 'Choisissez le type d\'objet que vous voulez importer :',
                'choices': self.liste_types
            },
            {
                'type': 'list',
                'name': 'objet',
                'message': f'Choisissez l\'objet que vous voulez importer :',
                'choices': AjoutObjVue.choix,
            }
        ]
        
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        nom_objet, description_objet = ObjetService.ImportObjetWeb(reponse['objet'])
        objet = DonjonService.ajouter_objet_et_recuperation_donjon(nom_objet, str(description_objet))
        dict_salles = MaitreDuJeuService.dict_salles() 
        print("Voici la liste des salles de votre donjon :")
        for salle in dict_salles:
            print(salle["nom_salle"], " : ", salle["id_salle"])
        identifiant_salle = input("Saisissez l'identifiant de la salle dans laquelle placer l'objet. \n")
        if DonjonService.existe_salle_donjon(identifiant_salle):
            DonjonService.ajouter_objet_salle(identifiant_salle, objet.id_objet)  
        from client.vue.donjon_vue import MenuDonjon
        return MenuDonjon()
        