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
Dragons Unfurled is a role-playing game (RPG) application based on the Dungeons and Dragons (D&D) 5th Edition universe. With Dragons Unfurled, only monsters can still stand in the way of your adventuring party. Your roleplayer will be able to join the adventure at any time, whether you are together or at a distance. 

The strength of this support is that it gives the game master the freedom to organise the campaign as they wish, with customisation ranging from simple character management to creating dungeons filled with monsters and treasure positioned to the exact square. Best of all, Dragons Unfurled allows you to save your games, as well as the characters and dungeons you create so that you can use them as you wish.

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
    <li><a href="#Implementation-plan">Implementation plan</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#licence">Licence</a></li>
    <li><a href="#contacts">Contacts</a></li>
    <li><a href="#resources">Resources</a></li>
  </ol>
</details>

<!-- A PROPOS DU PROJET -->
## Project structure

We will create one python file per class in the corresponding packages. This architecture allows a weak coupling between classes and a strong internal consistency. This will make the code more solid. Also, this structure will limit Git conflicts and offer better readability of the code.

For instance :
* The `business_object` package contains our 14 modules corresponding to the 14 business object classes. 
* The modules of the `service` package import those of the DAO package to manage the persistence of user actions. Our service package classes also use those of the web package.  
* The `web` package contains at least one search module to access our backend server.  
* The `vue` package imports services to call business functionality. We will have one module per vue. In particular, the abstract_vue module containing the AbstractVue class will provide a template for the vue classes that inherit from it. It will contain abstract methods for handling console display, menus and options.  
* The `test` package will contain a test module for the class "Grille". 
These are just a few explanations to get you started. All the packages, including routers, exceptions and images for example, are detailed in our report. :smile:


<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- MISE EN PLACE -->
## Setting up

Here is a way to install our application locally.
To run a local copy, follow these steps.

### Installation

1. Install PgAdmin 4 (or another tool to interact with the Postgres database sessions) and follow the steps to be ready to install a database
PostgreSQL locally.

2. Clone the repository and open it in your favorit source-code editor (like Visual Studio Code for instance).
   ```sh
   git clone https://github.com/Julien-Sklarik/Dragons-Unfurled.git 
   ```

3. Create your own `.env` file placed at the root of the project. To do so, copy and paste the content of the file `.env.template`.

4. Install the packages required.
   ```sh
   pip install -r requirements.txt
   ```
5. Run in PgAdmin the content of the file `init_bdd.sql`.
   
6. Split your terminal and run `app.py` in one of them.

7. If you wish, we encourage you to launch the `init_application.py` file in the second terminal, to add content for illustrative purposes in your database.

In particular, this file builds two initial administrator accounts. Indeed, we chose to create a file to create basic accounts rather than doing it directly on SQL 
to be able to hash the password with a hash function. 

8. Run the file `main.py` (interactively or by writing ``` python main.py ```) and enjoy Dragons Unfurled !

NB: You can run our unit tests to verify the operation of the Grid class by running the `test_grille.py` file from the `tests_unitaires` folder.
You can also look at our raw code. In particular, the business object `grille.py` is commented. This allows you to grasp the construction logic of our code.

<p align="right">(<a href="#top">Back to top</a>)</p>


<div id="utilis"></div>

### Authentication and Account Creation:

If you want to access all the features offered by the application, you need to identify yourself.
Nothing could be simpler, you are invited to connect or create an account.

### Create an account :

To create an account, all you have to do is select the account creation button from the first screen that appears.
- Step 1: Enter a username
- Step 2: Enter a valid password

NB: The password must have at least 6 characters, contain at least one upper case, one lower case and no special characters.

- Step 3: Confirm your password

Errors may occur when entering information (two passwords entered that are not identical,
information not respecting the required format ...). In this case, you will be asked to enter the information again.
But you only have 2 attempts, and in case of failure, we will be obliged to make you quit the application.

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- PLAN DE REALISATION -->
## Implementation plan

- [x] Implement the basic functionalities of the specifications
- [x] Implement the advanced features of the specifications
- [x] Complete the possibilities of administrators
     - [x] Banishment
     - [x] transfer of rights
- [x] Add an advanced automatic displacement system
- [x] Add a loading type animation

<p align="right">(<a href="#top">Back to top</a>)</p>

<div id="ref"></div>
<!-- CONTRIBUTION -->

## Contribution

Here is the contribution system to **Dragons Unfurled**.

If you want to contribute (once our project is in public mode), just make a pull request.

2. Create an Option branch (`git checkout -b option / NewOption`)
3. Do a Commit (`git commit -m 'add a NewOption'`)
4. Push on the branch (`git push origin option / NewOption`)
5. Make a pull request

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link : [https://github.com/Julien-Sklarik/Dragons-Unfurled.git](https://github.com/Julien-Sklarik/Dragons-Unfurled.git)

Email ENSAI - 

Julien Sklarik - julien.sklarik@eleve.ensai.fr

Manon Evain - evain.manon@eleve.ensai.fr

Loïc Bomo - loic.bomo@eleve.ensai.fr

Jules D'Haussy - jules.dhaussy@eleve.ensai.fr

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- RESSOURCES -->
## Ressources

Here are some resources we used to build this readme.

* [Choose an open source license](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Images Shields](https://shields.io)
* [Pages GitHub](https://pages.github.com)

<p align="right">(<a href="#top">Back to top</a>)</p>



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
