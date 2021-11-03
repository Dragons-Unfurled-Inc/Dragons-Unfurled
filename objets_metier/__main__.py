from objets_metier.entite import Entite
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.des import Des
from objets_metier.salle import Salle

caract = Caracteristique("Julien", "attack","capacité", "languages", "description")
essai = Personnage("classe","race","lore","id_joueur", "id_entite", "nomentite", caract)
#print(caract)
sall = Salle("id_salle", "nom_salle",None, [Objet("id_objet", "nom_objet","des"),Objet("id_objet2", "nom_objet2","des2")], [Entite("id joueur","id entite",caract)])
print(sall)

#print(essai)

#print(caract)