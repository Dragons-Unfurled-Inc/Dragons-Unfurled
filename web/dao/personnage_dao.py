from objets_metier.caracteristique import Caracteristique
from objets_metier.entite import Entite 
from objets_metier.personnage import Personnage
from web.dao.db_connection import DBConnection
from utils.singleton import Singleton

class PersonnageDAO(metaclass=Singleton):
    
    @staticmethod    
    def add_personnage(perso : Personnage) -> bool:
            created = False
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    personnage = Personnage(perso.classe,perso.race,perso.lore,perso.id_joueur,perso.id_entite,perso.nom_entite,Caracteristique.parse_obj(perso.caracteristiques_entite))
                    print(personnage)
                    cursor.execute(
                        "INSERT INTO personnages (classe, race,"\
                        "lore ,id_joueur ,id_entite,nom_entite ,niveau,experience,force,dexterite,constitution,intelligence,sagesse,charisme ,capacites ,vie ,attaques ,languages ,description) VALUES "\
                        "(%(classe)s, %(race)s, %(lore)s, %(id_joueur)s, %(id_entite)s, %(nom_entite)s,%(niveau)s, %(experience)s, %(force)s, %(dexterite)s, %(constitution)s, %(intelligence)s, %(sagesse)s, %(charisme)s, %(capacites)s, %(vie)s, %(attaques)s, %(languages)s, %(description)s)"\
                        
                    , {"classe" : personnage.classe
                    , "race": personnage.race
                    , "lore": personnage.lore
                    , "id_joueur": personnage.id_joueur
                    , "id_entite": personnage.id_entite
                    , "nom_entite": personnage.nom_entite
                    , "niveau": personnage.caracteristiques_entite.niveau
                    , "experience":personnage.caracteristiques_entite.experience
                    , "force":personnage.caracteristiques_entite.force
                    , "dexterite":personnage.caracteristiques_entite.dexterite
                    , "constitution":personnage.caracteristiques_entite.constitution
                    , "intelligence":personnage.caracteristiques_entite.intelligence
                    , "sagesse":personnage.caracteristiques_entite.sagesse
                    , "charisme":personnage.caracteristiques_entite.charisme
                    , "capacites":personnage.caracteristiques_entite.capacites
                    , "vie":personnage.caracteristiques_entite.vie
                    , "attaques":personnage.caracteristiques_entite.attaques
                    , "languages":personnage.caracteristiques_entite.languages
                    , "description":personnage.caracteristiques_entite.description
                    , })
             
            return created
