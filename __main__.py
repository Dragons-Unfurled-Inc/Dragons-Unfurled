from client.view.start_view import StartView


if __name__ == '__main__':
    # Lance notre première vue : StartView
    #test menu perso
    #current_view = MenuPersonnage(Joueur([],True,"bla","id",True,))
    current_view = StartView()

    # Tant que la vue n'est pas None, l'application continue de tourner.
    while current_view:
        # On affiche notre bordure entre chaque view.
        with open('client/dessins_ascii/border.txt', 'r', encoding="utf-8") as affichage1, open('client/dessins_ascii/logo_moyen.txt', 'r', encoding="utf-8") as affichage2:
            print(affichage1.read(),affichage2.read())
        # Nous Affichons les infos de la vue.
        current_view.display_info()
        # On demande à l'utilisateur son choix.
        current_view = current_view.make_choice()

    with open('client/dessins_ascii/logo.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
