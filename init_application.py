from client.service.campagne_service import CampagneService
from client.service.maitre_du_jeu_service import MaitreDuJeuService
from client.service.utilisateur_service import UtilisateurService
from client.vue.session import Session
from objets_metier.caracteristique import Caracteristique
from objets_metier.personnage import Personnage
from web.dao.entite_dao import EntiteDAO

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


# Trois personnages joueurs :

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

# Un personnage appartenant à Arthur :
Session.utilisateur.identifiant = "Arthur"
carac = Caracteristique(nom_entite = "Reciä Lanīakwæ")
personnage_arthur = Personnage(classe = "Druid",
                                race = "Half-Elf",
                                lore = "Reciä est une espèce de créateur, d'artiste même, qui serait capable d'insuffler la vie à des engrenages inertes... \n Il s'est promis de vaincre coûte que coûte.", 
                                id_joueur = "Arthur", 
                                id_entite = -1, 
                                nom_entite = "Reciä Lanīakwæ", 
                                caracteristiques_entite = carac) 
EntiteDAO.ajoute_entite(personnage_arthur)  

# Un deuxième personnage appartenant à Arthur :
carac = Caracteristique(nom_entite = "Hemmet")
personnage2_arthur = Personnage(classe = "Paladin",
                                race = "Human",
                                lore = "Il vécut son enfance comme écuyer d'un paladin et prit la voie de la chevalerie.", 
                                id_joueur = "Arthur", 
                                id_entite = -1, 
                                nom_entite = "Hemmet", 
                                caracteristiques_entite = carac) 
EntiteDAO.ajoute_entite(personnage2_arthur)  


# Deux campagnes :

# Une campagne de Arthur dont Thomas est joueur :
Session.utilisateur.identifiant = "Arthur"
MaitreDuJeuService.creer_campagne("Orbe mystérieuse !")
# Arthur ajoute le personnage de Thomas dans sa campagne : 
Session.id_campagne = 1
MaitreDuJeuService.ajouter_entite_campagne(1) # Thomas a dû transmettre à Arthur le nom et l'id de son personnage à ajouter.
CampagneService.mettre_joueur_dans_campagne("Thomas")

# La campagne de Isabelle :
Session.utilisateur.identifiant = "Isabelle"
MaitreDuJeuService.creer_campagne("Le royaume d'Isendar")
