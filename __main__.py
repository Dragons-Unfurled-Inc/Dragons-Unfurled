from client.vue.creation_compte_vue import CreaCompteVue
#from client.vue.creation_personnage_vue import MenuPersonnage
from client.vue.start_vue import StartVue
from objets_metier.joueur import Joueur

if __name__ == '__main__':
    # Lance notre première vue : StartVue
    current_vue = StartVue()
    #current_vue = CreaCompteVue()
    with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1,open('client/dessins_ascii/logo_moyen.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())
            
    # Tant que la vue n'est pas None, l'application continue de tourner.
    while current_vue:
    
        # Nous Affichons les infos de la vue.
        current_vue.display_info()
        
        # On demande à l'utilisateur son choix.
        current_vue = current_vue.make_choice()

    with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
