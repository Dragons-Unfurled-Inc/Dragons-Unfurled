from client.service.utilisateur_service import UtilisateurService


"""
Ce fichier sert à initialiser nos comptes administrateurs, ainsi que du contenu pratique pour découvrir notre application.
"""

# Deux comptes administrateurs initaux à l'état de tests.
UtilisateurService.creation_compte('Arthur','Arthur', True)
UtilisateurService.creation_compte('Alicia','Alicia', True)