from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.des import Des

caract = Caracteristique("Julien", "attack","capacité", "languages", "description")
essai = Personnage("classe","race","lore","id_joueur", "id_entite", "nomentite", caract)







print(essai)

#print(caract)