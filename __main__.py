from client.view.start_view import StartView
#from client.view.creation_personnage_view import MenuPersonnage
#from objets_metier.joueur import Joueur
from client.view.creation_compte_view import CreaCompteView

if __name__ == '__main__':
    # Lance notre première vue : StartView
    #test menu perso
    #current_view = MenuPersonnage(Joueur([],True,"bla","id",True,))
    current_view = StartView()
    #current_view = CreaCompteView()
    with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1,open('client/dessins_ascii/logo_moyen.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())
            
    # Tant que la vue n'est pas None, l'application continue de tourner.
    while current_view:
    
        # Nous Affichons les infos de la vue.
        current_view.display_info()
        
        # On demande à l'utilisateur son choix.
        current_view = current_view.make_choice()

    with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
