from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet

caract = Caracteristique("nom_entite", ["attack"], ["capacité"], ["languages"], "description")
obj = Objet("id_object", "nom_objet", "descr_objet")
essai = Personnage("classe","race","lore","id_joueur", "id_entite",caract,obj)
print(essai)