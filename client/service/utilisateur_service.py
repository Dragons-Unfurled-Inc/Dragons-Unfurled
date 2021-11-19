import hashlib
from getpass import getpass

from client.web_client.utilisateur_client import UtilisateurClient
from objets_metier.joueur import Joueur
from objets_metier.utilisateur import Utilisateur
#from objets_metier import utilisateur
from web.dao.utilisateur_dao import UtilisateurDAO

#import os
#from datetime import datetime



class UtilisateurService:
    """Cette classe fournit les services de création et de suppression
    de comptes aux utilisateurs, la connexion et la deconnexion."""

    @staticmethod
    def validation_creation_compte(nom_utilisateur,mot_de_passe,mot_de_passe2): # L'ensemble des conditions
        caractere = '[@_!#$%^&*()<>?/\|}{~:]'
        majuscule = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        minuscule = 'abcdefghijklmnopqrstuvxyz'
        validation = False

        if not validation:
            # nom_utilisateur = input("Veuillez entrer votre nom d'utilisateur : ")
            # mot_de_passe = getpass("Veuillez entrer votre mot de passe \n (Il doit contenir au moins cinq caractères dont une majuscule et une minuscules. Les charactères spéciaux ne sont pas autorisés.) :")
            # mot_de_passe2 = getpass("Veuillez confirmer votre mot de passe : ")

            if nom_utilisateur in UtilisateurDAO.liste_noms(): # Nous vérifions si ce nom d'utilisateur est déjà pris.
                print("Votre nom d'utilisateur a déjà été pris par une autre personne ! \n Veuillez choisir un autre nom, s'il vous plaît.")
                
            elif len(mot_de_passe) < 5:
                print("Votre mot de passe doit contenir au moins cinq caratères ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                
            elif len([x for x in mot_de_passe if x in majuscule]) < 1:
                print("Votre mot de passe doit comporter au moins une majuscule ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                
            elif len([x for x in mot_de_passe if x in minuscule]) < 1:
                print("Votre mot de passe doit comporter au moins une minuscule ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                
            elif len([x for x in mot_de_passe if x in caractere]) != 0:
                print("Votre mot de passe ne doit pas comporter de caractère spécial ! \n Veuillez choisir un autre mot de passe, s'il vous plaît.")
                
            elif mot_de_passe2 != mot_de_passe:
                print("Vous n'avez pas entré deux fois le même mot de passe ! \n Veuillez recommencer, s'il vous plaît.")
                
            else:
                validation = True
                
        return validation
        #à stocker dans un objet session plus tard

    @staticmethod
    def creation_compte(nom_utilisateur: str, mot_de_passe_utilisateur: str, est_admin: bool = False):
        # if compte != None:
        #     if type_compte == "joueur":
        #         nouvel_utilisateur = Utilisateur(connecte = True,
        #                                         mot_de_passe = compte[1],
        #                                         identifiant = compte[0],
        #                                         est_administrateur = False,
        #                                         feed_backs = True
        #                                         )  
        #     elif type_compte == "administrateur":
        #         nouvel_utilisateur = Utilisateur(connecte = False,
        #                                         mot_de_passe = compte[1],
        #                                         identifiant = compte[0],
        #                                         est_administrateur = True,
        #                                         feed_backs = True)
        mdp_hash = mot_de_passe_utilisateur.encode() # Hachage du mot de passe
        mdp = hashlib.sha256()
        mdp.update(mdp_hash)
        from client.vue.session import Session
        Session.utilisateur = Utilisateur(identifiant = nom_utilisateur)  
        utilisateur = Session.utilisateur           
        mot_de_passe = mdp.hexdigest()
        UtilisateurClient.creation_utilisateur(utilisateur.identifiant, mot_de_passe, est_admin) 
        # return nouvel_utilisateur
        # else:
        #     print("Votre compte n'a pas pu être créé !")

    @staticmethod
    def connexion(nom_utilisateur: str, mot_de_passe_utilisateur: str):
        existe = UtilisateurClient.est_utilisateur(nom_utilisateur)
        if not existe == True: 
            print('Cet utilisateur n\'existe pas')
            return False
        pass_hash = mot_de_passe_utilisateur.encode()
        mdp = hashlib.sha256()
        mdp.update(pass_hash)
        if UtilisateurClient.bon_mot_de_passe(nom_utilisateur, mdp.hexdigest()) == True:
            from client.vue.session import Session
            Session.utilisateur = Joueur(identifiant = nom_utilisateur)
            return True
        return False 

    @staticmethod
    def est_admin(nom_utilisateur: str):
        est_administrateur = UtilisateurClient.est_administrateur(nom_utilisateur)
        if est_administrateur == True:
            return True
        return False
    