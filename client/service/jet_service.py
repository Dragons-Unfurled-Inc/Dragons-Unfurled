class JetService:
    def __init__(self, lanceur, 
                       nombre,
                       faces,
                       cible) -> None:
        self.__lanceur = lanceur
        self.__nombre = nombre 
        self.__faces = faces
        self.__cible = cible 
        self.__resultat = nombre*[0]
        
    def __str__(self):
        """
        permet un affichage du lancer de dés
        """
        modele = '\n'.join([
            'Le joueur {} a lancé {} dé(s) et obtenu {}.'.format(
            self.__lanceur,
            self.__nombre,
            self.__faces,
            self.__resultat),
            "Le dés à {} faces à fait {}"]).format(
            self.__faces,
            self.__resultat_des)
        return modele

    def attaquer(self):
        None

    @property
    def lanceur(self):
        return self.__lanceur
    
    @lanceur.setter
    def lanceur(self, value):
        self.__lanceur = value

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def faces(self):
        return self.__faces
    
    @faces.setter
    def faces(self, value):
        self.__faces = value

    @property
    def resultat(self):
        return self.__resultat
    
    @resultat.setter
    def resultat(self, value):
        self.__resultat = value