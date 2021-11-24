import requests
from client.web_client.web_configuration import WebConfiguration


class UtilisateurClient:

    @staticmethod
    def creation_utilisateur(utilisateur_nom, mot_de_passe, est_administrateur):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/creation_utilisateur", api_url)
        est_un_utilisateur = requests.post(api_dest, json = {'utilisateur_nom': utilisateur_nom, 'mot_de_passe' : mot_de_passe, 'est_administrateur' : est_administrateur})
        return est_un_utilisateur.json()
        
    @staticmethod
    def est_utilisateur(nom: str):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/utilisateur/{}",api_url,nom)
        est_un_utilisateur = requests.get(api_dest)
        resultat = est_un_utilisateur.json()
        return resultat
 
    @staticmethod
    def est_administrateur(nom: str) :
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/administrateur/{}",api_url,nom)
        est_un_administrateur = requests.get(api_dest)
        resultat = est_un_administrateur.json()
        return resultat

    @staticmethod
    def bon_mot_de_passe(utilisateur_nom, mot_de_passe):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/utilisateur/{}/mot_de_passe/{}", api_url, utilisateur_nom, mot_de_passe)
        mdp_juste = requests.get(api_dest)
        resultat = mdp_juste.json()
        return resultat
