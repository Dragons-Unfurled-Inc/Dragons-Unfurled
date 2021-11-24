import requests
from client.vue.session import Session
from client.web_client.web_configuration import WebConfiguration


class FeedBackClient:

    @staticmethod
    def consulter_tous_les_feed_backs():
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/feed_backs",api_url)
        feed_backs = requests.get(api_dest)
        resultat = feed_backs.json()
        return resultat

    @staticmethod
    def donne_feedback(identifiant_joueur: int, message: str) :
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/donne_feed_back", api_url)
        requests.post(api_dest, json = {'message': message, 'identifiant_joueur': identifiant_joueur})

    @staticmethod
    def consulter_feed_back():
        id_joueur = Session.utilisateur.identifiant
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/feed_backs/id_joueur/{}", api_url, id_joueur)
        feed_backs = requests.get(api_dest)
        resultat = feed_backs.json()
        return resultat
