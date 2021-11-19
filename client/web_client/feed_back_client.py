import requests
from client.web_client.web_configuration import WebConfiguration


class FeedBackClient:

    # @staticmethod
    # def consulter_un():
    #     configuration = WebConfiguration()
    #     api_url = configuration.getApiUrl()
    #     api_dest = str.format("http://{}/feed_back/{}/mot_de_passe/{}/est_administrateur/{}", api_url, feed_back_nom, mot_de_passe, est_administrateur)
    #     requests.post(api_dest)
        
    @staticmethod
    def consulter_tous_les_feed_backs():
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/feed_backs",api_url)
        feed_backs = requests.get(api_dest)
        resultat = feed_backs.json()
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
    def bon_mot_de_passe(feed_back_nom, mot_de_passe):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/feed_back/{}/mot_de_passe/{}", api_url, feed_back_nom, mot_de_passe)
        mdp_juste = requests.get(api_dest)
        resultat = mdp_juste.json()
        return resultat
