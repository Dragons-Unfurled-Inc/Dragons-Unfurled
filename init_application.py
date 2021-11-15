from client.service.utilisateur_service import UtilisateurService


"""
Ce fichier sert à initialiser nos comptes administrateurs, ainsi que du contenu pratique pour découvrir notre application.
"""

# Deux comptes administrateurs initaux.
UtilisateurService.creation_compte('Arthur','Arthur', True)
UtilisateurService.creation_compte('Alicia','Alicia', True)

# Un compte joueur.
UtilisateurService.creation_compte('Thomas','Thomas', False)
UtilisateurService.creation_compte('Isabelle','Isabelle', False)