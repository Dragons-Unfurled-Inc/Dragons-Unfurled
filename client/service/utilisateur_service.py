#import hashlib
#from getpass import getpass
#from datetime import datetime

from objets_metier import utilisateur
from web.dao.utilisateur_dao import UtilisateurDao
#from dao.compte_dao import CompteDAO
from objets_metier.utilisateur import Utilisateur
from exceptions.utilisateur_non_authentifie_exception import UtilisateurNonAuthentifie


class UtilisateurService:
    """Cette classe fournit les services de création et de suppression
    de comptes aux utilisateurs, la connexion et la deconnexion"""

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

            if nom_utilisateur in CompteDAO.liste_noms(): # Nous vérifions si ce nom d'utilisateur est déjà pris.
                print("Votre nom d'utilisateur a déjà été pris par une autre personne ! \n Veuillez choisir un autre nom s'il vous plaît.")
                continue

            elif len(mot_de_passe) < 5:
                print("Votre mot de passe doit contenir au moins cinq caratères ! \n Veuillez choisir un autre mot de passe s'il vous plaît.")
                continue

            elif len([x for x in mot_de_passe if x in majuscule]) < 1:
                print("Votre mot de passe doit comporter au moins une majuscule ! \n Veuillez choisir un autre mot de passe s'il vous plaît.")
                continue

            elif len([x for x in mot_de_passe if x in minuscule]) < 1:
                print("Votre mot de passe doit comporter au moins une minuscule ! \n Veuillez choisir un autre mot de passe s'il vous plaît.")
                continue

            elif len([x for x in mot_de_passe if x in caractere]) != 0:
                print("Votre mot de passe ne doit pas comporter de caractère ! \n Veuillez choisir un autre mot de passe s'il vous plaît.")
                continue

            elif mot_de_passe2 != mot_de_passe:
                print("Vous n'avez pas entré deux fois le même mot de passe ! \n Veuillez recommencer s'il vous plaît.")
                continue

            else:
                validation = True

        # Hachage du mot de passe
        mdp_hash = mot_de_passe.encode()
        mdp = hashlib.sha256()
        mdp.update(mdp_hash)
        compte_user = [nom_utilisateur, mdp.digest()]
        return compte_user

    @staticmethod
    def CreateCompte(type_compte):
        compte = utilisateur_service.validation_creation_compte()
        if not compte == None:
            if type_compte == "client":
                new_user = Client(id_user=None,
                                  name=compte[0],
                                  pass_hash=compte[1],
                                  type_compte=type_compte,
                                  solde=0,
                                  date_last_connexion=datetime.now()
                                  )
            elif type_compte == "administrateur":
                new_user = Administrateur(id_user=None,
                                          name=compte[0],
                                          pass_hash=compte[1],
                                          type_compte=type_compte,
                                          solde=0,
                                          date_last_connexion=datetime.now()
                                          )

            CompteDAO.CreateCompte(new_user)

            print("Votre compte a pu être créé avec succès")
        else:
            print("Votre compte n'a pas pu être créé !")

    @staticmethod
    def DelateCompte(nom_utilisateur):
        CompteDAO.DeleteCompte(nom_utilisateur)


    @staticmethod
    def connexion(nom_utilisateur, i):
        if nom_utilisateur == None:
            nom_utilisateur = input("Quel est votre pseudonyme ? ")
        if nom_utilisateur not in CompteDAO.listeNoms():
            print("Ce compte n'existe pas")
            print("Veuillez réessayer \n")
            return utilisateur_service.connexion(None, i)
        else:
            compte_user = CompteDAO.readCompte(nom_utilisateur)
            mot_de_passe_user = getpass("Veuillez entrez votre mot de passe : ")
            pass_hash = mot_de_passe_user.encode()
            m = hashlib.sha256()
            m.update(pass_hash)
            if m.digest() == bytes(CompteDAO.readCompte(nom_utilisateur)[2][:]):
                if compte_user[3] == "client":
                    user = Client(id_user=compte_user[0],
                                  name=compte_user[1],
                                  pass_hash=compte_user[2],
                                  type_compte="client",
                                  solde=compte_user[4],
                                  date_last_connexion=compte_user[5])
                    return user
                elif compte_user[3] == "administrateur":
                    user = Administrateur(id_user=compte_user[0],
                                          name=compte_user[1],
                                          pass_hash=compte_user[2],
                                          type_compte="administrateur",
                                          solde=compte_user[4],
                                          date_last_connexion=compte_user[5])
                    return user
            else:
                print("Votre mot de passe est incorrect !")
                if i < 2:
                    print("Veuillez réessayer \n (il vous reste {} essais possibles)".format(2-i))
                    return utilisateur_service.connexion(nom_utilisateur,i+1)
                else:
                    print("Vous avez atteint le nombre maximum d'essais")
                    print("Nous sommes contraint de vous faire quitter l'application")
                    import sys
                    sys.exit()

    @staticmethod
    def deconnexion(nom):
        date_derniere_connexion = str(datetime.now())
        CompteDAO.UpdateCompte(nom, 'derniere_connexion', date_derniere_connexion)

    @staticmethod
    def createutilisateur(utilisateur: Utilisateur) -> Utilisateur:
        return UtilisateurDao.createutilisateur(utilisateur)

    @staticmethod
    def authenticate_and_get_utilisateur(utilisateur_nom: str, mot_de_passe: str) -> Utilisateur:
        if (UtilisateurDao.verifyPassword(utilisateur_nom, mot_de_passe)):
            return UtilisateurDao.getutilisateur(utilisateur_nom)
        else:
            raise UtilisateurNonAuthentifie(utilisateur_nom=utilisateur_nom)
