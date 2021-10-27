class UtilisateurIntrouvableException(Exception):
    """
    Exception levée quand l'utilisateur est introuvable
    """

    def __init__(self, utilisateur_nom: str):
        self.message = "Utilisateur "+utilisateur_nom + " introuvable"
        super().__init__(self.message)
