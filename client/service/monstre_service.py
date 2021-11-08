import requests as requ
from objets_metier.caracteristique import Caracteristique
from web.dao.monstre_dao import MonstreDAO 
from objets_metier.monstre import Monstre


class MonstreService():
    
    @staticmethod
    def ImportMonstreWeb(nom = str):
        req = requ.get('https://www.dnd5eapi.co/api/monsters/' + nom)
        d=req.json()
        return (Monstre(d["type"],0,0,Caracteristique(d['name'],d['actions'],d['senses'],d['languages'],d['special_abilities']+d['legendary_actions'],'')))
    
    @staticmethod
    def ImportMonstreParType(triche = bool):
        if triche :
            return {'aberration': ['aboleth', 'chuul', 'cloaker', 'gibbering-mouther', 'otyugh'], 'humanoid': ['acolyte', 'archmage', 'assassin', 'bandit', 'bandit-captain', 'berserker', 'bugbear', 'commoner', 'cult-fanatic', 'cultist', 'deep-gnome-svirfneblin', 'drow', 'druid', 'duergar', 'gladiator', 'gnoll', 'goblin', 'grimlock', 'guard', 'half-red-dragon-veteran', 'hobgoblin', 'knight', 'kobold', 'lizardfolk', 'mage', 'merfolk', 'noble', 'orc', 'priest', 'sahuagin', 'scout', 'spy', 'thug', 'tribal-warrior', 'veteran', 'werebear-bear', 'werebear-human', 'werebear-hybrid', 'wereboar-boar', 'wereboar-human', 'wereboar-hybrid', 'wererat-human', 'wererat-hybrid', 'wererat-rat', 'weretiger-human', 'weretiger-hybrid', 'weretiger-tiger', 'werewolf-human', 'werewolf-hybrid', 'werewolf-wolf'], 'dragon': ['adult-black-dragon', 'adult-blue-dragon', 'adult-brass-dragon', 'adult-bronze-dragon', 'adult-copper-dragon', 'adult-gold-dragon', 'adult-green-dragon', 'adult-red-dragon', 'adult-silver-dragon', 'adult-white-dragon', 'ancient-black-dragon', 'ancient-blue-dragon', 'ancient-brass-dragon', 'ancient-bronze-dragon', 'ancient-copper-dragon', 'ancient-gold-dragon', 'ancient-green-dragon', 'ancient-red-dragon', 'ancient-silver-dragon', 'ancient-white-dragon', 'black-dragon-wyrmling', 'blue-dragon-wyrmling', 'brass-dragon-wyrmling', 'bronze-dragon-wyrmling', 'copper-dragon-wyrmling', 'dragon-turtle', 'gold-dragon-wyrmling', 'green-dragon-wyrmling', 'pseudodragon', 'red-dragon-wyrmling', 'silver-dragon-wyrmling', 'white-dragon-wyrmling', 'wyvern', 'young-black-dragon', 'young-blue-dragon', 'young-brass-dragon', 'young-bronze-dragon', 'young-copper-dragon', 'young-gold-dragon', 'young-green-dragon', 'young-red-dragon', 'young-silver-dragon', 'young-white-dragon'], 'elemental': ['air-elemental', 'azer', 'djinni', 'dust-mephit', 'earth-elemental', 'efreeti', 'fire-elemental', 'gargoyle', 'ice-mephit', 'invisible-stalker', 'magma-mephit', 'magmin', 'salamander', 'steam-mephit', 'water-elemental', 'xorn'], 'monstrosity': ['androsphinx', 'ankheg', 'basilisk', 'behir', 'bulette', 'centaur', 'chimera', 'cockatrice', 'darkmantle', 'death-dog', 'doppelganger', 'drider', 'ettercap', 'gorgon', 'grick', 'griffon', 'guardian-naga', 'gynosphinx', 'harpy', 'hippogriff', 'hydra', 'kraken', 'lamia', 'manticore', 'medusa', 'merrow', 'mimic', 'minotaur', 'owlbear', 
'phase-spider', 'purple-worm', 'remorhaz', 'roc', 'roper', 'rust-monster', 'spirit-naga', 'tarrasque', 'winter-wolf', 'worg'], 'construct': ['animated-armor', 'clay-golem', 'flesh-golem', 'flying-sword', 'homunculus', 'iron-golem', 'rug-of-smothering', 'shield-guardian', 'stone-golem'], 'beast': ['ape', 'axe-beak', 'baboon', 'badger', 'bat', 'black-bear', 'blood-hawk', 'boar', 'brown-bear', 'camel', 'cat', 'constrictor-snake', 'crab', 'crocodile', 'deer', 'dire-wolf', 'draft-horse', 'eagle', 'elephant', 'elk', 'flying-snake', 'frog', 'giant-ape', 'giant-badger', 'giant-bat', 'giant-boar', 'giant-centipede', 'giant-constrictor-snake', 'giant-crab', 'giant-crocodile', 'giant-eagle', 'giant-elk', 'giant-fire-beetle', 'giant-frog', 'giant-goat', 'giant-hyena', 'giant-lizard', 'giant-octopus', 'giant-owl', 'giant-poisonous-snake', 'giant-rat', 'giant-rat-diseased', 'giant-scorpion', 'giant-sea-horse', 'giant-shark', 'giant-spider', 'giant-toad', 'giant-vulture', 'giant-wasp', 'giant-weasel', 'giant-wolf-spider', 'goat', 'hawk', 'hunter-shark', 'hyena', 'jackal', 'killer-whale', 'lion', 'lizard', 'mammoth', 'mastiff', 'mule', 'octopus', 'owl', 'panther', 'plesiosaurus', 'poisonous-snake', 'polar-bear', 'pony', 'quipper', 'rat', 'raven', 'reef-shark', 'rhinoceros', 'riding-horse', 'saber-toothed-tiger', 'scorpion', 'sea-horse', 'spider', 'stirge', 'tiger', 'triceratops', 'tyrannosaurus-rex', 'vulture', 'warhorse', 'weasel', 'wolf'], 'plant': ['awakened-shrub', 'awakened-tree', 'shambling-mound', 'shrieker', 'treant', 'violet-fungus'], 'fiend': ['balor', 'barbed-devil', 'bearded-devil', 'bone-devil', 'chain-devil', 'dretch', 'erinyes', 'glabrezu', 'hell-hound', 'hezrou', 'horned-devil', 'ice-devil', 'imp', 'lemure', 'marilith', 'nalfeshnee', 'night-hag', 'nightmare', 'pit-fiend', 'quasit', 'rakshasa', 'succubus-incubus', 'vrock'], 'ooze': ['black-pudding', 'gelatinous-cube', 'gray-ooze', 'ochre-jelly'], 'fey': ['blink-dog', 'dryad', 'green-hag', 'satyr', 'sea-hag', 'sprite'], 'giant': ['cloud-giant', 'ettin', 'fire-giant', 'frost-giant', 'hill-giant', 'ogre', 'oni', 'stone-giant', 'storm-giant', 'troll'], 'celestial': ['couatl', 'deva', 'pegasus', 'planetar', 'solar', 'unicorn'], 'undead': ['ghast', 'ghost', 'ghoul', 'lich', 'minotaur-skeleton', 'mummy', 'mummy-lord', 'ogre-zombie', 'shadow', 'skeleton', 'specter', 'vampire', 'vampire-spawn', 'warhorse-skeleton', 'wight', 'will-o-wisp', 'wraith', 'zombie'], 'swarm of Tiny beasts': ['swarm-of-bats', 'swarm-of-beetles', 'swarm-of-centipedes', 'swarm-of-insects', 'swarm-of-poisonous-snakes', 'swarm-of-quippers', 'swarm-of-rats', 'swarm-of-ravens', 'swarm-of-spiders', 'swarm-of-wasps']}

        monstres = requ.get('https://www.dnd5eapi.co/api/monsters')
        monstres = monstres.json()
        nom_monstres = [d["index"] for d in monstres["results"]]
        monstres_par_types = {}
        for monstre in nom_monstres : 
            dic_monstre = requ.get('https://www.dnd5eapi.co/api/monsters/' + monstre)
            dic_monstre = dic_monstre.json()
            type_monstre = dic_monstre["type"]
            if type_monstre not in monstres_par_types:
                monstres_par_types[type_monstre] = [monstre]
            else :
                monstres_par_types.update({type_monstre : monstres_par_types[type_monstre]+[monstre]})
        return(monstres_par_types)
    
    @staticmethod
    def ImportListeTypes():
        return (MonstreService.ImportMonstreParType(True).keys())