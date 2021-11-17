from client.service.personnage_service import PersonnageService
from client.service.utilisateur_service import UtilisateurService
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

# Deux comptes joueurs.
UtilisateurService.creation_compte('Thomas','Thomas', False)
UtilisateurService.creation_compte('Isabelle','Isabelle', False)

# Trois personnages.
carac = Caracteristique("Gilthar Arcal")
personnage_thomas = Personnage("Wizard",
                                "Elf",
                                "Les années d'apprentissage ont apaisées le jeune Gilthar, il n'est plus malveillant mais possède toujours les traits de caractère de son enfance.", 
                                "Thomas", 
                                -1, 
                                "Gilthar Arcal", 
                                carac) 
EntiteDAO.add_entite(personnage_thomas)   

carac = Caracteristique("Reciä Lanīakwæ")
personnage_arthur = Personnage("Druid",
                                "Half-Elf",
                                "Reciä est une espèce de créateur, d'artiste même, qui serait capable d'insuffler la vie à des engrenages inertes... \n Il s'est promis de vaincre coûte que coûte.", 
                                "Arthur", 
                                -1, 
                                "Reciä Lanīakwæ", 
                                carac) 
EntiteDAO.add_entite(personnage_arthur)  

carac = Caracteristique("Hemmet Shaw")
personnage2_arthur = Personnage("Paladin",
                                "Human",
                                "Il vécut son enfance comme écuyer d'un paladin et prit la voie de la chevalerie.", 
                                "Arthur", 
                                -1, 
                                "Hemmet Shaw", 
                                carac) 
EntiteDAO.add_entite(personnage2_arthur)  
