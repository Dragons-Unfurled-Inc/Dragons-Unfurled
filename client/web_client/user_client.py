import os
from typing import List

import requests
from client.exceptions.utilisateur_non_authentifie_exception import \
    UtilisateurNonAuthentifie
from client.web_client.web_configuration import WebConfiguration
from objets_metier.utilisateur import Utilisateur
from web.service.utilisateur_service import UtilisateurService


class UtilisateurClient:

    # @staticmethod
    # def createUtilisateur(user: Utilisateur) -> Utilisateur:
        
    #     r = requests.get("http://localhost:5000")  

    #     return UtilisateurDao.createUtilisateur(user)

    # @staticmethod
    # def authenticate_and_get_user(username: str, password: str) -> Utilisateur:
    #     if (UtilisateurDao.verifyPassword(username, password)):
    #         return UtilisateurDao.getUtilisateur(username)
    #     else:
    #         raise UtilisateurNonAuthentifie(username=username)

    @staticmethod
    def createUtilisateur(user: Utilisateur) :
        pass

    @staticmethod
    def authenticate_and_get_user(username: str, password: str) :
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("{}/users/{}",api_url,username)
        userAsDict = requests.get(api_dest)
        return userAsDict

    @staticmethod
    def updateUtilisateur(user: Utilisateur)-> None:
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("{}/users/{}",api_url,user.identifiant)
        userAsDict = requests.post(api_dest)
        
    @staticmethod
    def deleteUtilisateur(user:Utilisateur):
        pass

    @staticmethod
    def getAllUtilisateurs() :
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("{}/users",api_url)
        usersAsDict = requests.get(api_dest)
        usersAsDict = usersAsDict.json()
        users = []
        for userAsDict in usersAsDict:
            users.append(UtilisateurClient.userDictToUtilisateur(userAsDict))
        return users

    @staticmethod
    def userDictToUtilisateur(user_as_dict: dict) -> Utilisateur:
        return Utilisateur(user_as_dict["id"],user_as_dict["username"],user_as_dict["password"])
