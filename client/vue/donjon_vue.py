from client.service.donjon_service import DonjonService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.objet_service import ObjetService
from client.vue.abstract_vue import AbstractVue
from client.vue.session import Session

from web.service.salle_service import SalleService

from objets_metier.donjon import Donjon

from PyInquirer import Separator, prompt



class MenuDonjon(AbstractVue):

    def __init__(self):

        utilisateur = Session.utilisateur
        self.id_campagne = Session.id_campagne
        self.id_donjon = Session.id_donjon


        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': f' {utilisateur.identifiant} que souhaitez-vous faire ?',
                'choices': [
                    'Afficher le donjon',
                    'Consulter une salle',
                    'Ajouter une salle',
                    'Modifier une salle',
                    Separator(),
                    'Ajouter un élément dans une salle du donjon',
                    'Ramasser un objet avec un personnage',
                    'Déplacer ou retirer un élément',
                    Separator(),
                    'Quitter le donjon',
                    
                ]
            }, 
            {
                'type': 'confirm',
                'name': 'construction',
                'message': 'Voulez-vous construire la forme de votre salle en entrant les coordonnées des cellules une à une ?',
                'default': False
            }
        ]
    
    def display_info(self):
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/texte/ecran_donjon.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())

    def make_choice(self):
        reponse = prompt(self.__questions[0])
        if reponse['choix'] == 'Afficher le donjon':
            donjon = DonjonService.trouver_donjon(self.id_donjon)
            print(donjon)
            from client.vue.donjon_vue import MenuDonjon
            return MenuDonjon()

        if reponse['choix'] == 'Consulter une salle': 
            dict_salles = DonjonService.dict_salles()
            print("Voici les salles disponibles:")
            for salle in dict_salles:
                print(salle["nom_salle"],' : ',salle["id_salle"])
            id_salle = input("Saisissez l'identifiant de la salle à consulter. \n")
            existe_salle = DonjonService.existe_salle_donjon(id_salle)
            if existe_salle:
                print("Voici le contenu de la salle:")
                salle = SalleService.trouve_salle(id_salle)
                print(salle)
            else:
                print("La salle entrée est introuvable.")
            from client.vue.donjon_vue import MenuDonjon 
            return MenuDonjon()

        if reponse['choix'] == 'Ajouter une salle':
            construction = prompt(self.__questions[1])["construction"]
            nom_salle =  input("Saisissez le nom de la salle à créer. \n")  
            x = int(input("Saisissez l'abscice x de la salle pour la positionner dans votre donjon. \nPar exemple, la salle principale a pour coordonnées x = 0, y = 0.\n"))
            y = int(input("Saisissez l'ordonnée y de la salle pour la positionner dans votre donjon. \nPar exemple, la salle principale a pour coordonnées x = 0, y = 0.\n"))
            if DonjonService.espace_libre_salle(x,y): 
                if construction:
                    nb_cell = input("Saisissez le nombre de cellules que vous comptez placer.\n")
                    coord_cellules = []
                    for i in range(int(nb_cell)):
                        cell_x = input("Saissisez la coordonnée x de votre cellule n°" + str(i) + "\n")
                        cell_y = input("Saissisez la coordonnée y de votre cellule n°" + str(i) + "\n")
                        coord_cellules.append([cell_x, cell_y])
                    Donjon.ajouter_salle_construite(x, y , nom_salle, coord_cellules)
                else:
                    largeur = int(input("Saisissez la largeur de la salle. \n"))
                    profondeur = int(input("Saisissez la profondeur de la salle. \n"))
                    Donjon.ajouter_salle_rectangulaire(largeur, profondeur, nom_salle, x, y)
                print("La salle a bien été ajoutée.")
            else:
                print("La place était déjà prise.")
            from client.vue.donjon_vue import MenuDonjon 
            return MenuDonjon()

        if reponse['choix'] == 'Modifier une salle':
            dict_salles = DonjonService.dict_salles()
            print("Voici les salles disponibles:")
            for salle in dict_salles:
                print(salle["nom_salle"],' : ',salle["id_salle"])
            id_salle = input("Saisissez l'identifiant de la salle à consulter. \n")
            salle = SalleService.trouve_salle(id_salle)
            Donjon.editer_salle(self.id_donjon, salle)
            from client.vue.modif_salle_vue import ModifSalleVue
            return ModifSalleVue(id_salle)

        if reponse['choix'] == 'Ajouter un élément dans une salle du donjon':
            from client.vue.donjon_vues.ajout_vue import MenuAjout
            return MenuAjout()

        if reponse['choix'] == 'Ramasser un objet avec un personnage':
            dict_objets = MaitreDuJeuService.dict_objets()  
            print("Voici la liste des différents objets :")
            for objet in dict_objets:
                print(objet["nom_objet"], " : ", objet["id_objet"])
            identifiant_objet = input("Saisissez l'identifiant de l'objet à ramasser. \n")
            identifiant_salle = MaitreDuJeuService.id_salle_contenant_objet(identifiant_objet)   
            if identifiant_salle == None:
                print("L'objet entré n'est dans aucune salle.")
            else:
                dict_entites = MaitreDuJeuService.dict_entites()
                print("Voici la liste des différentes entités :")
                for entite in dict_entites:
                    print(entite["nom_entite"], " : ", entite["id_entite"])
                identifiant_entite = input("Saisissez l'identifiant de l'entité qui récupère l'objet. \n")
                dict_salles = MaitreDuJeuService.dict_salles() 
                if DonjonService.existe_entite_campagne(identifiant_entite):
                    ObjetService.ramasse_objet(identifiant_entite, identifiant_objet)  
                    print("L'objet a été ramassé.")
                else:
                    print("L'identifiant entré ne correspond pas à une entité de la campagne.")
            from client.vue.donjon_vue import MenuDonjon 
            return MenuDonjon()

        if reponse['choix'] == 'Déplacer ou retirer un élément':
            from client.vue.donjon_vues.deplace_vue import MenuDeplace
            return MenuDeplace()

        if reponse['choix'] == 'Quitter le donjon':
            from client.vue.maitre_du_jeu_vue import MenuMJ
            return MenuMJ()
      