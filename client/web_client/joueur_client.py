import requests
from client.web_client.web_configuration import WebConfiguration


class JoueurClient:

    @staticmethod
    def liste_noms():
        configuration = WebConfiguration()
        api_url = configuration.getApiUrl()
        api_dest = str.format("http://{}/joueurs", api_url)
        joueurs = requests.get(api_dest)
        resultat = joueurs.json()
        return resultat
