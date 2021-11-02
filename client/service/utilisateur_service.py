#import hashlib
#from getpass import getpass
#from datetime import datetime

from objets_metier import utilisateur
from web.dao.utilisateur_dao import UtilisateurDao
#from dao.compte_dao import CompteDAO
from objets_metier.utilisateur import Utilisateur
from exceptions.utilisateur_non_authentifie_exception import UtilisateurNonAuthentifie


class UtilisateurService:
    """Cette classe s'occupe des services de base d'un utilisateur : la création et la suppression
    d'un compte, la connxion et la deconnexion"""

    @staticmethod
    def validation_creation_compte():
        ####emsemble des choses à vérifier##
        majuscule = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        minuscule = 'abcdefghijklmnopqrstuvxyz'
        char = '[@_!#$%^&*()<>?/\|}{~:]'
        while True:

            valid = 0

            user_name = input("Veuillez entrez votre nom : ")

            password = getpass(
                "Entrez un mot de passe (Doit contenir au moins 6 caractères avec 1 majuscules, 1 minuscules, charactères spéciaux interdits):")
            password2 = getpass("Confirmer votre mot de passe : ")

            if user_name in CompteDAO.listeNoms(): ##condition d'utilisateur déjà existant dans la base #
                print("Le nom que vous souhaitez utiliser a déjà été pris par un autre utilisateur !")
                print("Veuillez en choisir un autre")

                continue

            elif len(password) < 6:
                print("Mot de passe trop court!")

                continue


            elif not len([x for x in password if x in majuscule]) >= 1:
                print("Votre mot de passe doit comportez au minimum une majuscule!")

                continue

            elif not len([x for x in password if x in minuscule]) >= 1:
                print("Votre mot de passe doit comportez au minimum une majuscule!")

                continue

            elif not len([x for x in password if x in char]) == 0:
                print("Entrez un mot de passe valide!")

                continue

            elif not password2 == password:
                print("Vos mots de passe ne correspondent pas")

                continue

            else:
                valid = True
                break

        if valid == True:

            ## Hachage du mot de passe

            pass_hash = password.encode()
            m = hashlib.sha256()
            m.update(pass_hash)
            compte_user = [user_name, m.digest()]
            return compte_user
        else:
            return None

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
    def DelateCompte(user_name):
        CompteDAO.DeleteCompte(user_name)


    @staticmethod
    def connexion(user_name, i):
        if user_name == None:
            user_name = input("Quel est votre pseudonyme ? ")
        if user_name not in CompteDAO.listeNoms():
            print("Ce compte n'existe pas")
            print("Veuillez réessayer \n")
            return utilisateur_service.connexion(None, i)
        else:
            compte_user = CompteDAO.readCompte(user_name)
            password_user = getpass("Veuillez entrez votre mot de passe : ")
            pass_hash = password_user.encode()
            m = hashlib.sha256()
            m.update(pass_hash)
            if m.digest() == bytes(CompteDAO.readCompte(user_name)[2][:]):
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
                    return utilisateur_service.connexion(user_name,i+1)
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
    def authenticate_and_get_utilisateur(utilisateur_nom: str, password: str) -> Utilisateur:
        if (UtilisateurDao.verifyPassword(utilisateur_nom, password)):
            return UtilisateurDao.getutilisateur(utilisateur_nom)
        else:
            raise UtilisateurNonAuthentifie(utilisateur_nom=utilisateur_nom)
