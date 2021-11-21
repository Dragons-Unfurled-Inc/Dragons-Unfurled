import requests
from client.vue.session import Session
from client.web_client.web_configuration import WebConfiguration


class AdministrateurClient:

    @staticmethod
    def supprimer_droits_administrateur(nom_administrateur_donneur: str):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/administrateur/termine/{}", api_url, nom_administrateur_donneur)
        requests.patch(api_dest)

    @staticmethod
    def ajouter_droits_administrateur(nom_administrateur):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/administrateur/nouveau/{}", api_url, nom_administrateur)
        requests.patch(api_dest)

    @staticmethod
    def supprimer_compte(nom_utilisateur):
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/bannir/{}", api_url, nom_utilisateur)
        requests.delete(api_dest)