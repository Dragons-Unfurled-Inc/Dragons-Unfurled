<div id="top"></div>

<!-- Presentation-->
<!--
*** For readability, we use the markdown "reference style".
*** For example, we will put our references in square brackets [ ] rather than parentheses ( ).
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
Dragons Unfurled is a role-playing game (RPG) application based on the Dungeons and Dragons (D&D) 5th Edition universe. With Dragons Unfurled , only monsters can still stand in the way of your adventuring party. Your roleplayer will be able to join the adventure at any time, whether you are together or at a distance. 

The strength of this support is that it gives the game master the freedom to organise the campaign as they wish, with customisation ranging from simple character management to creating dungeons filled with monsters and treasure positioned to the exact square. Best of all, Dragons Unfurled allows you to save your games, as well as the characters and dungeons you create, so that you can use them as you wish.

As well as adding to the application's base, any user can contribute by sending feedback to the team of administrators who are there to ensure that your gaming experience is optimal. Using the data provided by the open D&D 5th Edition API, Dragons Unfurled brings the arsenal of D&D RPGs to your fingertips.
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
      <a href="#Project-structure">Project structure</a>
    </li>
    <li>
      <a href="#Setting-up">Setting-up</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Accessing-the-application">Accessing the application</a></li>
    <li><a href="#Implementation-plan">Implementation plan</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#licence">Licence</a></li>
    <li><a href="#contacts">Contacts</a></li>
    <li><a href="#resources">Resources</a></li>
  </ol>
</details>

<!-- A PROPOS DU PROJET -->
## Project structure

We will create one python file per class in the corresponding packages. This architecture allows a weak coupling between classes and a strong internal consistency. This will make the code more solid. Also, this structure will limit Git conflicts and offer a better readability of the code.

* The `business_object` package contains our 13 modules corresponding to the 13 business object classes. 
* The modules of the `service` package import those of the DAO package to manage the persistence of user actions. Our service package classes also use those of the web package.  
* The `web` package contains at least one search module to access our back-end server.  
* The `vue` package imports services to call business functionality. We will have one module per vue. In particular, the abstract_vue module containing the AbstractVue class will provide a template for the vue classes that inherit from it. It will contain abstract methods for handling console display, menus and options.  
* The `test` package will contain a test module for each layer of our application. :smile:


<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- MISE EN PLACE -->
## Setting up

Here is a way to install our application locally.
To run a local copy, follow these steps.

### Installation

1. Install PgAdmin 4 and follow the steps to install our database
PostgreSQL locally.
2. Clone the repository
   ```sh
   git clone https://github.com/Julien-Sklarik/Dragons-Unfurled.git 
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Run in PgAdmin the content of the file `init_bdd.sql`
   
5. Split your terminal and

### Accessing the application :

For a first use of our application, the following steps have to be done:
- 1: Open the VS Code terminal
- 2: Execute the SQL script [init_base.sql] to create the database tables (db) in PgAdmin 4,

NB: You can also use another database provided that you update the database properties.
To do this, go to [properties] in the [configuration] folder to modify the database properties.

- 3: Remember to install libraries from the general installation.
- 4: Run the `createCompte` file placed at the root of the project to create the basic accounts by writing in the terminal :
```
python3 createCompte.py
```
Indeed, we chose to create a file to create basic accounts rather than doing it directly on SQL 
to be able to hash the password with a hash function. 
 
You can now run our application!
Either by running the main.py file, or by running :
```
python main.py
```
NB: Remember to run our unit tests to check the application works, by running
the test_Services package file of the test package : []

You can also look at our raw code which we have commented out. 
We have commented in more detail the class in the file []. This allows you to grasp the construction logic of our code.

<p align="right">(<a href="#top">Back to top</a>)</p>


<div id="utilis"></div>

### Authentification et Création de compte:

Si vous souhaitez accéder à l’ensemble des fonctionnalités offertes par l’application, il vous faut vous identifier.
Pour cela, rien de plus simple, vous êtes invités à vous connecter ou à vous créer un compte.

### Créer un compte :

Pour créer un compte, sélectionnez la commande me créer un compte du menu principal
- Etape 1 : Renseigner un identifiant
- Etape 2 : Renseigner un mot de passe valide
NB: le mot de passe doit avoir au moins 6 caractères, contenir au moins une Majuscule, une minuscule et pas de caractères spéciaux.
- Etape 3 : Confirmer votre mot de passe

Des erreurs peuvent survenir lors de la saisie des informations (deux mots de passe renseignés non identiques,
information ne respectant pas le format requis...). Dans ce cas, il vous sera demandé de saisir l’information de nouveau.
Mais vous n'avez que 2 tentatives, et en cas d'échec, nous serons contraint de vous faire quitter l'application.

<p align="right">(<a href="#top">Retourner en haut de page</a>)</p>



<!-- PLAN DE REALISATION -->
## Implementation plan

- [x] Implémenter les fonctionnalités de base du cahier des charges 
- [x] Implémenter les fonctionnalités avancées du cahier des charges 
- [x] Compléter les possibilités des administrateurs
    - [x] Banissement
    - [x] transfert des droits
- [x] Ajouter un système de déplacement automatique avancée 
- [x] Ajouter une animation de type chargement

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
