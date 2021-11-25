##### il reste les cas d'utilisations à modifier/adapter et l'installation à modifier. + tout relire


<div id="top"></div>

<!-- Présentation -->
<!--
*** Pour la lisibilité, nous utilisons le markdown "reference style".
*** Nous allons par exemple mettre nos références entre crochets [ ] plutôt qu'entre parenthèses ( ).
-->
[![JDR][jdr]][jdr-url]
[![API][d&d]][d&d-url]
[![Contributeurs][contributeurs]][contributeurs-url]
[![MIT Licence][licence]][licence-url]



<!-- PROJET LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" >
  </a>

  <h3 align="center">Dragons Unfurled</h3>

  <p align="center">
Dragons Unfurled est une application pour jeux de rôles (JDR) basée sur l’univers de Donjons et Dragons (D&D) 5e édition. Grâce à Dragons Unfurled , seuls les monstres pourront encore barrer la route à votre troupe d’aventuriers. Vos rôlistes pourront rejoindre l’aventure à tout moment, que vous soyez réunis ou à distance. 

La force de ce support est d’offrir la liberté au maître du jeu d’organiser la campagne comme il le souhaite, la personnalisation pouvant aller de la simple gestion des personnages à la création de donjons remplis de monstres et de trésors positionnés à la case près. Mieux encore, Dragons Unfurled permet de sauvegarder vos parties, mais aussi les personnages et donjons que vous créez pour que vous puissiez vous en servir à votre guise.

En plus d’étoffer la base de l’application, tout utilisateur peut contribuer en envoyant un feedback à l’équipe d’administrateurs qui est là pour veiller à ce que votre expérience de jeu soit optimale. Employant les données fournies par l’API ouverte D&D 5th Edition API, Dragons Unfurled déploie l’arsenal du JDR D&D à portée de main.
    <br />
    <a href="https://github.com/Dragons-Unfurled-Inc"><strong>Dragons Unfurled Inc. »</strong></a>
    <br />
    <br />
    <a href="#instal">Installation</a>
    ·
    <a href="#utilis">Utilisation </a>
    ·
    <a href="#ref">Références</a>
  </p>
</div>


<!-- SOMMAIRE -->
<details>
  <summary>Sommaire</summary>
  <ol>
    <li>
      <a href="#Structure-du-projet">Structure du projet</a>
      <ul>
        <li><a href="#utilisé-lors-de-l'implémentation-du-code">Utilisé lors de l'implémentation du code</a></li>
      </ul>
    </li>
    <li>
      <a href="#mise-en-place">Mise en place</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#utilisation">Utilisation</a></li>
    <li><a href="#plan-de-réalisation">Plan de réalisation</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#licence">Licence</a></li>
    <li><a href="#contacts">Contacts</a></li>
    <li><a href="#ressources">Ressources</a></li>
  </ol>
</details>



<!-- A PROPOS DU PROJET -->
## Structure du projet

Nous allons créer un fichier python par classe dans les packages correspondants. Cette architecture permet un faible couplage entre les classes et une forte cohérence interne. Le code s’en trouvera plus solide. Aussi, cette structure permettra de limiter les conflits Git et d’offrir une meilleure lisibilité du code.

* Le package `objet_metier` contient nos 13 modules correspondants aux 13 classes d’objets métiers. 
* Les modules du package `service` importent ceux du package DAO pour gérer la persistance des actions des utilisateurs. Nos classes du package service utilisent aussi celles du package web. 
* Le package `web` contient au moins un module de recherche pour accéder à notre serveur back-end. 
* Le package `vue` importe les services pour appeler les fonctionnalités métiers. Nous aurons un module par vue. Notamment, le module abstract_vue contenant la classe AbstractVue offrira un modèle aux classes de vue qui en héritent. Elle contiendra des méthodes abstraites pour gérer l’aﬀichage en console, les menus et les options. 
* Le package `test` contiendra un module de tests pour chaque couche de notre application. :smile:


<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



### Utilisé lors de l'implémentation du code

Cette section va présenter nos outils de développements.

* [Visual Studio Code](https://code.visualstudio.com/)

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>


<!-- MISE EN PLACE -->
## Mise en place

Voici une manière d'installer notre application localement.
Pour lancer une copie locale, suivez les étapes suivantes.

### Installation

1. Optenez une clef pour l'API [https://www.dnd5eapi.co/](https://www.dnd5eapi.co/)
2. Cloner le repertoire
   ```sh
   git clone https://github.com/Julien-Sklarik/Dragons-Unfurled.git 
   ```
3. Installer les packages
   ```sh
   pip install -r requirements.txt
   ```
   ou alors, faites:
   ```
   pip install requests
   pip install psycopg2-binary
   pip install PyInquirer
   ```
4. Enter l'API dans `config.js`
   ```js
   const API_KEY = 'D&D 5e API';
   ```

### Accéder à l’application :

Pour une première utilisation de notre application, il faut réaliser les étapes suivantes :
- 1 : Ouvrir le terminal de VS Code
- 2 : Exécuter le script SQL [init_base.sql] pour créer les tables de la base de données (bdd),

NB : Vous pouvez aussi utiliser une autre base à condition de mettre à jour les propriétés de la bdd.
Pour ce faire, allez dans [proprietes] du dossier [configuration] pour modifier les propriétés de la bdd.

- 3 : Pensez à installer des librairies de l'installation générale.
- 4 : Lancer le fichier `createCompte` placé à la racine du projet pour créer les comptes de base en écrivant dans le terminal :
```
python3 createCompte.py
```
Effectivement, nous avons choisit de créer un fichier pour créer des comptes de base plutôt que de le faire directement sur SQL 
pour pouvoir hacher le mot de passe avec une fonction de hachage. 
 
Vous pouvez désormais exécuter notre application !
Soit en lançant le fichier main.py, soit en exécutant :
```
python main.py
```
NB : Pensez à exécuter nos tests unitaires pour vérifier le fonctionnement de l'application, en lançant
le fichier du package test_Services du package test : [Services_test.py]

Vous pouvez aussi regarder notre code brute que nous avons pris soin de commenter. 
Nous avons commenté de façons plus détaillé la classe du fichier [PersonnageService.py]. Ceci permet de saisir la logique de construction de notre code.

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>


<div id="utilis"></div>

<!-- UTILISATION EXAMPLES -->

## Utilisation

Voici des exemple d'utilisations possibles de notre application :

### Authentification et Création de compte:

Si vous souhaitez accéder à l’ensemble des fonctionnalités offertes par l’application, il vous faut vous identifier.
Pour cela, rien de plus simple, vous êtes invités à vous connecter ou à vous créer un compte.

#### Se connecter :

Pour vous connecter, sélectionnez la commande "Me connecter" puis renseignez votre email et votre mot
de passe. En cas d’erreur, l'application renvoie un message "email incorrect" ou "mot de passe incorrect". 
Vous pouvez saisir vos informations de nouveau.
Le mot de passe est crypté donc ne vous inquiétez pas si vous ne le voyez pas lors de votre saisie.

#### Créer un compte :

Pour créer un compte, sélectionnez la commande me créer un compte du menu principal
- Etape 1 : Renseigner un identifiant
- Etape 2 : Renseigner un mot de passe valide
NB: le mot de passe doit avoir au moins 5 caractères, contenir au moins une Majuscule, une minuscule et pas de caractères spéciaux.
- Etape 3 : Confirmer votre mot de passe

Des erreurs peuvent survenir lors de la saisie des informations (deux mots de passe renseignés non identiques,
information ne respectant pas le format requis...). Dans ce cas, il vous sera demandé de saisir l’information de nouveau.
Mais vous n'avez que 2 tentatives, et en cas d'échec, nous serons contraint de vous faire quitter l'application.


<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



<!-- PLAN DE REALISATION -->
## Plan de réalisation

- [x] Implémenter les fonctionnalités de base du cahier des charges 
- [x] Implémenter les fonctionnalités avancées du cahier des charges 
- [] Compléter les possibilités des administrateurs
    - [] Banissement
    - [] transfert des droits
- [] Ajouter un système de gestion d'argent

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>

<div id="ref"></div>
<!-- CONTRIBUTION -->

## Contribution

Voici le système de contribution à **Dragons Unfurled**.

Si vous voulez contribuer (une fois notre projet passé en mode publique), il suffit de faire une requête pull.

2. Créer une branche Option (`git checkout -b option/NouvelleOption`)
3. Faites un Commit (`git commit -m 'ajouter une NouvelleOption'`)
4. Pousser sur la branche (`git push origin option/NouvelleOption`)
5. Faites une requête Pull

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



<!-- LICENSE -->
## License

Distribué sous la licence MIT. Regardez `LICENSE.txt` pour plus d'informations.

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



<!-- CONTACT -->
## Contact

Lien du projet : [https://github.com/Julien-Sklarik/Dragons-Unfurled.git](https://github.com/Julien-Sklarik/Dragons-Unfurled.git)

Email ENSAI - 

Julien Sklarik - julien.sklarik@eleve.ensai.fr

Manon Evain - evain.manon@eleve.ensai.fr

Loïc Bomo - loic.bomo@eleve.ensai.fr

Jules D'Haussy - jules.dhaussy@eleve.ensai.fr

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



<!-- RESSOURCES -->
## Ressources

Voici une liste de ressources que nous avons utilisées pour le développement de notre projet.

* [Choisir une licence Open Source](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Images Shields](https://shields.io)
* [Pages GitHub](https://pages.github.com)

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



<!-- MARKDOWN LIENS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributeurs]: https://img.shields.io/badge/Contributeurs-4-green
[contributeurs-url]: https://github.com/Julien-Sklarik/Dragons-Unfurled.git
[jdr]: https://img.shields.io/badge/JDR-D&D5e-red
[jdr-url]: https://www.dnd5eapi.co/docs/
[d&d]: https://img.shields.io/badge/API-D&D5eAPI-9cf
[d&d-url]: https://www.dnd5eapi.co/
[licence]: https://img.shields.io/badge/Licence-MIT-inactive
[licence-url]: https://github.com/Julien-Sklarik/Dragons-Unfurled/blob/dad41cc124244de403fe19cee0abdd8fb52f6beb/LICENSE
