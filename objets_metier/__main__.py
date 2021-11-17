from datetime import datetime

from objets_metier.donjon import Donjon
from objets_metier.entite import Entite
from objets_metier.monstre import Monstre
from objets_metier.personnage import Personnage
from objets_metier.caracteristique import Caracteristique
from objets_metier.objet import Objet
from objets_metier.des import Des
from objets_metier.salle import Salle

caract = Caracteristique(nom_entite="Nom", attaques=["Attaques"], capacites=["Capacité"], languages=["langages"],description="des")
perso = Personnage(classe = "classe", race = "race",lore = "lore",id_joueur = 0, id_entite = 0, nom_entite = "nomentite", caracteristiques_entite = caract)
obj = Objet(id_objet = "id_objet", nom_objet = "nom_objet",description_obj = "des")
monstr = Monstre(type = "type",id_joueur = 'id',id_entite = 'id',caracteristiques_entite = caract)
enti = Entite("id joueur","id entite",caract, [obj])
sall = Salle("id_salle", "nom_salle",None, [Objet("id_objet", "nom_objet","des"),Objet("id_objet2", "nom_objet2","des2")], [Entite("id joueur","id entite",caract, [obj])])
donj = Donjon("id_donjon", "nom_donjon", [sall])
#des = Des(4)

print(caract)
#print(perso)
#print(enti)
#print(sall)
#print(obj)
#print(donj)
#print(monstr)
#print(feed)

