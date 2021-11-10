import hashlib
from getpass import getpass
#import os
#from datetime import datetime

#from objets_metier import utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO
from objets_metier.utilisateur import Utilisateur


class UtilisateurService:
    """Cette classe fournit les services de création et de suppression
    de comptes aux utilisateurs, la connexion et la deconnexion."""

    @staticmethod
    def validation_creation_compte(): # L'ensemble des conditions
        caractere = '[@_!#$%^&*()<>?/\|}{~:]'
        majuscule = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        minuscule = 'abcdefghijklmnopqrstuvxyz'
        validation = False

        while not validation:
            nom_utilisateur = input("Veuillez entrer votre nom d'utilisateur : ")
            mot_de_passe = getpass("Veuillez entrer votre mot de passe \n (Il doit contenir au moins cinq caractères dont une majuscule et une minuscules. Les charactères spéciaux ne sont pas autorisés.) :")
            mot_de_passe2 = getpass("Veuillez confirmer votre mot de passe : ")

            if nom_utilisateur in UtilisateurDAO.liste_noms(): # Nous vérifions si ce nom d'utilisateur est déjà pris.
                print("Votre nom d'utilisateur a déjà été pris par une autre personne ! \n Veuillez choisir un autre nom, s'il vous plaît.")
                continue

            elif len(mot_de_passe) < 5:
                print("Votre mot de passe doit contenir au moins cinq caratères ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                continue

            elif len([x for x in mot_de_passe if x in majuscule]) < 1:
                print("Votre mot de passe doit comporter au moins une majuscule ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                continue

            elif len([x for x in mot_de_passe if x in minuscule]) < 1:
                print("Votre mot de passe doit comporter au moins une minuscule ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                continue

            elif len([x for x in mot_de_passe if x in caractere]) != 0:
                print("Votre mot de passe ne doit pas comporter de caractère ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                continue

            elif mot_de_passe2 != mot_de_passe:
                print("Vous n'avez pas entré deux fois le même mot de passe ! \n Veuillez recommencer, s'il vous plaît.")
                continue

            else:
                validation = True

        mdp_hash = mot_de_passe.encode() # Hachage du mot de passe
        mdp = hashlib.sha256()
        mdp.update(mdp_hash)
        compte_utilisateur = [nom_utilisateur, mdp.digest()]
        return compte_utilisateur

    @staticmethod
    def creation_compte(type_compte):
        compte = UtilisateurService.validation_creation_compte()
        if compte != None:
            if type_compte == "joueur":
                nouvel_utilisateur = Utilisateur(connecte = False,
                                                mot_de_passe = compte[1],
                                                identifiant = compte[0],
                                                est_administrateur = False)  
            elif type_compte == "administrateur":
                nouvel_utilisateur = Utilisateur(connecte = False,
                                                mot_de_passe = compte[1],
                                                identifiant = compte[0],
                                                est_administrateur = True) 
            UtilisateurDAO.creation_compte(nouvel_utilisateur)
            print("Votre compte a été créé avec succès !")
        else:
            print("Votre compte n'a pas pu être créé !")

    @staticmethod
    def connexion(nom_utilisateur = None, tentative_num: int = 1):
        if nom_utilisateur == None:
            nom_utilisateur = input("Quel est votre nom d'utilisateur ? ")
        if nom_utilisateur not in UtilisateurDAO.liste_noms():
            print("Ce nom d'utilisateur n'existe pas ! \n Veuillez réessayer, s'il vous plaît.")
            return UtilisateurService.connexion(None, tentative_num)
        else:
            compte_utilisateur = UtilisateurDAO.getUtilisateur(nom_utilisateur)
            mot_de_passe_utilisateur = getpass("Veuillez entrer votre mot de passe, s'il vous plaît : ")
            pass_hash = mot_de_passe_utilisateur.encode()
            mdp = hashlib.sha256()
            mdp.update(pass_hash)
            if mdp.digest() == bytes(UtilisateurDAO.getUtilisateur(nom_utilisateur)[2][:]):
                if compte_utilisateur[3] == "joueur":
                    utilisateur = Utilisateur(connecte = True,
                                                mot_de_passe = compte_utilisateur[1],
                                                identifiant = compte_utilisateur[0],
                                                est_administrateur = False)
                    return utilisateur
                elif compte_utilisateur[3] == "administrateur":
                    utilisateur = Utilisateur(connecte = True,
                                                mot_de_passe = compte_utilisateur[1],
                                                identifiant = compte_utilisateur[0],
                                                est_administrateur = True)
                    return utilisateur
            else:
                print("Votre mot de passe est incorrect.")
                if tentative_num < 2:
                    print("Veuillez réessayer, s'il vous plaît. \n (il vous reste {} essais possibles)".format(2-tentative_num))
                    return UtilisateurService.connexion(nom_utilisateur,tentative_num+1)
                else:
                    print("Vous avez fait le nombre d'essais maximal. \n Vous allez être déconnecté.")
                    import sys
                    sys.exit()