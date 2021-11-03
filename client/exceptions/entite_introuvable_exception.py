class EntiteIntrouvableException(Exception):
    """
    Exception levée quand l'entite est introuvable
    """
    def __init__(self, entite_nom: str):
        self.message = "".join("L'entite ",entite_nom,"est introuvable.")
        super().__init__(self.message)