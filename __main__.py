#Test2

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
import matplotlib.pyplot as plt

print("Dans l'affichage interactif suivant, ne cliquez pas sur l'option choisie mais sélectionnez-la avec les flèches de votre clavier, sinon cela produira une erreur.")
def choix(answers):
    options = []
    if answers['theme'] == 'Utiliser notre programme dans le cas générale':
        options.append('Faites \"entrer\"')
    if answers['theme'] == "Observer des exemples d'utilisation sur les jeux de données proposés dans le sujet":
        options.append('Quel est le nombre total d’hospitalisations dues au Covid-19 ?')
        options.append('Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ?')
        options.append('Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à celle de la semaine dernière ?')
        options.append('Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours ?')
        options.append('Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020 ?')
        options.append("Regarder tout les exemples")
    if answers['theme'] == "Observer des exemples supplémentaires illustratifs d'utilisation qui mettent en valeur la conception de votre programme":
        options.append("Y a-t-il une différence entre les sommes des totaux de personnes hospitalisez dues au Covid-19 entre les tables \"donnees-hospitalieres-covid19-2021-03-03-17h03.csv\" et \"donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv\" ?")
        options.append("Créer un nouveau fichier .csv et sauvegardez dessus le résultat des k-means avec k = 5 sur les données des départements du mois de Mars 2021, lissées avec une moyenne glissante de 5 jours")
        options.append("Quel est le département et la date avec le plus grand nombre de décès ?")
        options.append("Afficher l'histogramme des cas de décès par départements du mois de Mars 2021")
        options.append("Afficher les données sur fond de carte")
        options.append("Regarder tout les exemples")
    return options

questions = [{'type': 'list',
            'name': 'theme',
            'message': 'Que voulez-vous faire ?',
            'choices': ['Utiliser notre programme dans le cas générale',
                        Separator(),
                        "Observer des exemples d'utilisation sur les jeux de données proposés dans le sujet",
                        "Observer des exemples supplémentaires illustratifs d'utilisation qui mettent en valeur la conception de votre programme",]},
    {
        'type': 'list',
        'name': 'specification',
        'message': 'Précision :',
        'choices': choix,
    },]

answers = prompt(questions, style=custom_style_2)
print(answers)

import datetime
from datetime import date
import random
random.seed(123) # A enlever si vous voulez des résultats aléatoire et différent des notre pour les KMeans

# Cas générale d'utilisation :

import os # Utilisé ici uniquement pour changer le répertoire de travail.

wd = input("Souhaitez-vous changer le répertoire de travail pour simplifier les adresses de fichier ? \n Si c'est le cas, entrez la nouvelle adresse.\n Sinon, faites \"entrer\" :\n")
if wd:
    os.chdir(wd)

#### Dans mon cas
os.chdir("/Users/juliensklarik/Projet informatique")
####