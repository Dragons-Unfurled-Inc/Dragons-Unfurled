class UtilisateurNonAuthentifie(Exception):
    """Exception levée quand l'utilisateur n'est pas authentifié
    """

    def __init__(self, utilisateur_nom: str):
        self.message = "L'utilisateur "+utilisateur_nom + " ne peut pas être authentifié"
        super().__init__(self.message)
