class UtilisateurIntrouvableException(Exception):
    """
    Exception levée quand l'utilisateur est introuvable
    """
    def __init__(self, utilisateur_nom: str):
        self.message = ("L' utilisateur est introuvable.")
        super().__init__(self.message)
