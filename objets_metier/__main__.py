from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet

caract = Caracteristique("nom_entite", "attack","capacité", "languages", "description")
essai = Personnage("classe","race","lore","id_joueur", "id_entite",caract)
print(essai)