from client.service.campagne_service import CampagneService
from client.service.donjon_service import DonjonService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.objet_service import ObjetService
from client.service.utilisateur_service import UtilisateurService
from client.vue.session import Session
from objets_metier.caracteristique import Caracteristique
from objets_metier.donjon import Donjon
from objets_metier.objet import Objet
from objets_metier.personnage import Personnage
from web.dao.entite_dao import EntiteDAO
from web.dao.objet_dao import ObjetDAO

"""
Ce fichier sert à initialiser nos comptes administrateurs, ainsi que du contenu pratique pour découvrir notre application.
"""

# Voici nos deux comptes administrateurs initaux :

UtilisateurService.creation_compte('Arthur','Arthur', True)
UtilisateurService.creation_compte('Alicia','Alicia', True)


# Ci-dessous se trouve le contenu pratique pour découvrir notre application :

# Deux comptes joueurs :
UtilisateurService.creation_compte('Thomas','Thomas', False)
UtilisateurService.creation_compte('Isabelle','Isabelle', False)


# Quelques personnages joueurs :

# Un personnage appartenant à Thomas :
Session.utilisateur.identifiant = "Thomas"
carac = Caracteristique(nom_entite = "Gilthar", description = "Gilthar est un magicien de 2 metres qui aime l'aventure !")
personnage_thomas = Personnage(classe = "Wizard",
                                race = "Elf",
                                lore = "Les années d'apprentissage ont apaisées le jeune Gilthar, il n'est plus malveillant mais possède toujours les traits de caractère de son enfance.", 
                                id_joueur = "Thomas", 
                                id_entite = -1, # Nous l'inition à -1 mais la base de données va lui en attribuer un autre automatiquement.
                                nom_entite = "Gilthar", 
                                caracteristiques_entite = carac) 
EntiteDAO.ajoute_entite(personnage_thomas)   

#Une reproduction de ce personnage pour que Thomas ai une dizaine de personnages identiques :
for _ in range(9):
    EntiteDAO.ajoute_entite(personnage_thomas)    

# Un personnage appartenant à Arthur :
Session.utilisateur.identifiant = "Arthur"
carac = Caracteristique(nom_entite = "Reciä Lanīakwæ")
personnage_arthur = Personnage(classe = "Druid",
                                race = "Half-Elf",
                                lore = "Reciä est une espèce de créateur, d'artiste même, qui serait capable d'insuffler la vie à des engrenages inertes...", 
                                id_joueur = "Arthur", 
                                id_entite = -1, 
                                nom_entite = "Reciä Lanīakwæ", 
                                caracteristiques_entite = carac) 
EntiteDAO.ajoute_entite(personnage_arthur)  

#Une reproduction de ce personnage pour que Arthur ai une vintaine de personnages identiques :
for _ in range(19):
    EntiteDAO.ajoute_entite(personnage_arthur)

# Un personnage appartenant à Isabelle répliqué 10 fois:
Session.utilisateur.identifiant = "Isabelle"
carac = Caracteristique(nom_entite = "Hemmet")
personnage_isabelle = Personnage(classe = "Paladin",
                                race = "Human",
                                lore = "Il vécut son enfance comme écuyer d'un paladin et prit la voie de la chevalerie.", 
                                id_joueur = "Isabelle", 
                                id_entite = -1, 
                                nom_entite = "Hemmet", 
                                caracteristiques_entite = carac) 
for _ in range(10):
    EntiteDAO.ajoute_entite(personnage_isabelle)   


# Deux campagnes :

# Deux campagne d'Arthur dont Thomas est joueur :
Session.utilisateur.identifiant = "Arthur"
MaitreDuJeuService.creer_campagne("Orbe mystérieuse !")
MaitreDuJeuService.creer_campagne("Orbe mystérieuse le retour !")

# Arthur ajoute le personnage de Thomas dans sa campagne, ainsi que ses personnages, les PNJ qu'il a créés : 
Session.id_campagne = 1
MaitreDuJeuService.ajouter_entite_campagne(1) # Thomas a dû transmettre à Arthur le nom et l'id de son personnage à ajouter.
CampagneService.mettre_joueur_dans_campagne("Thomas")
for k in range(11,31):
    MaitreDuJeuService.ajouter_entite_campagne(k)

# Une campagne d'Isabelle :
Session.utilisateur.identifiant = "Isabelle"
MaitreDuJeuService.creer_campagne("Le royaume d'Isendar")

# Un donjon d'Arthur :
Session.utilisateur.identifiant = "Arthur"
Session.id_campagne = 1
DonjonService.construire_donjon("Le phare", 20, 10)
Session.id_donjon = 1

# Une salle "sur mesures" dans le donjon d'Arthur :
Donjon.ajouter_salle_construite(0, 1 , "L'entre du dragon", [[2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [9, 9], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14], [11, 9], [11, 10], [11, 11], [11, 12], [11, 13], [11, 14], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [13, 14], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [17, 9], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [18, 9], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [21, 9], [21, 10], [21, 11], [21, 12], [21, 13], [21, 14], [22, 9], [22, 10], [22, 11], [22, 12], [22, 13], [22, 14], [23, 9], [23, 10], [23, 11], [23, 12], [23, 13], [23, 14], [24, 9], [24, 10], [24, 11], [24, 12], [24, 13], [24, 14], [25, 9], [25, 10], [25, 11], [25, 12], [25, 13], [25, 14], [26, 9], [26, 10], [26, 11], [26, 12], [26, 13], [26, 14], [27, 9], [27, 10], [27, 11], [27, 12], [27, 13], [27, 14], [28, 9], [28, 10], [28, 11], [28, 12], [28, 13], [28, 14], [29, 9], [29, 10], [29, 11], [29, 12], [29, 13], [29, 14], [14, 5], [14, 6], [14, 7], [14, 8], [15, 5], [15, 6], [15, 7], [15, 8], [16, 5], [16, 6], [16, 7], [16, 8], [17, 5], [17, 6], [17, 7], [17, 8], [21, 1], [21, 2], [21, 3], [21, 4], [21, 5], [21, 6], [22, 1], [22, 2], [22, 3], [22, 4], [22, 5], [22, 6], [23, 1], [23, 2], [23, 3], [23, 4], [23, 5], [23, 6], [24, 1], [24, 2], [24, 3], [24, 4], [24, 5], [24, 6], [25, 1], [25, 2], [25, 3], [25, 4], [25, 5], [25, 6], [26, 1], [26, 2], [26, 3], [26, 4], [26, 5], [26, 6], [27, 1], [27, 2], [27, 3], [27, 4], [27, 5], [27, 6], [28, 1], [28, 2], [28, 3], [28, 4], [28, 5], [28, 6], [29, 1], [29, 2], [29, 3], [29, 4], [29, 5], [29, 6], [30, 1], [30, 2], [30, 3], [30, 4], [30, 5], [30, 6], [11, 3], [11, 4], [12, 3], [12, 4], [13, 3], [13, 4], [14, 3], [14, 4], [15, 3], [15, 4], [16, 3], [16, 4], [17, 3], [17, 4], [18, 3], [18, 4], [19, 3], [19, 4], [20, 3], [20, 4], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6]])

# Nous plaçons 21 entités dans la salle sur mesure d'Arthur puis nous les déplaçons maintenant jusqu'à des cases choisies :
DonjonService.deplacer_entite_dans_salle(1, 2, [1, 1]) 
DonjonService.deplacer_entite_dans_salle(11, 2, [2,2]) 
DonjonService.deplacer_entite_dans_salle(12, 2, [27,11]) 
DonjonService.deplacer_entite_dans_salle(13, 2, [15, 10]) 
DonjonService.deplacer_entite_dans_salle(14, 2, [8,4]) 
DonjonService.deplacer_entite_dans_salle(15, 2, [16,10]) 
DonjonService.deplacer_entite_dans_salle(16, 2, [22,4]) 
DonjonService.deplacer_entite_dans_salle(17, 2, [6, 11]) 
DonjonService.deplacer_entite_dans_salle(18, 2, [9, 11]) 
DonjonService.deplacer_entite_dans_salle(19, 2, [10, 11]) 
DonjonService.deplacer_entite_dans_salle(20, 2, [11, 11]) 
DonjonService.deplacer_entite_dans_salle(21, 2, [14, 11]) 
DonjonService.deplacer_entite_dans_salle(22, 2, [15, 11]) 
DonjonService.deplacer_entite_dans_salle(23, 2, [16, 11]) 
DonjonService.deplacer_entite_dans_salle(24, 2, [17, 11]) 
DonjonService.deplacer_entite_dans_salle(25, 2, [20, 11]) 
DonjonService.deplacer_entite_dans_salle(26, 2, [21, 11]) 
DonjonService.deplacer_entite_dans_salle(27, 2, [25, 11]) 
DonjonService.deplacer_entite_dans_salle(28, 2, [25, 11]) 
DonjonService.deplacer_entite_dans_salle(29, 2, [25, 11]) 
DonjonService.deplacer_entite_dans_salle(30, 2, [25, 11])

# Un objet répliqué 15 fois qu'Arthur va placer dans cette salle :

objet_arthur = Objet(id_objet = -1,nom_objet = "sac d'or", description_obj = "Une quantitée aléatoire de pièces d'ors. Cela peut monter jusau'à 8 000 pièces !")

for _ in range(15):
    ObjetDAO.ajouter_objet(objet_arthur)

DonjonService.deplacer_objet_dans_salle(1, 2, [15,3])
DonjonService.deplacer_objet_dans_salle(2, 2, [19,9])
DonjonService.deplacer_objet_dans_salle(3, 2, [29,2])
DonjonService.deplacer_objet_dans_salle(4, 2, [2, 14])
DonjonService.deplacer_objet_dans_salle(5, 2, [3, 14])
DonjonService.deplacer_objet_dans_salle(6, 2, [4, 14])
DonjonService.deplacer_objet_dans_salle(7, 2, [15, 14])
DonjonService.deplacer_objet_dans_salle(8, 2, [16, 14])
DonjonService.deplacer_objet_dans_salle(9, 2, [27, 14])
DonjonService.deplacer_objet_dans_salle(10, 2, [28, 14])
DonjonService.deplacer_objet_dans_salle(11, 2, [29, 14])

DonjonService.deplacer_objet_dans_salle(12, 2, [5, 14])
DonjonService.deplacer_objet_dans_salle(13, 2, [6, 14])
DonjonService.deplacer_objet_dans_salle(14, 2, [7, 14])

# Gilthar, le personnage de thomas, va ramasser trois objets dans la salle du donjon d'Arthur :
ObjetService.ramasse_objet(1, 12) 
ObjetService.ramasse_objet(1, 13)
ObjetService.ramasse_objet(1, 14) 
