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

We will create one python file per class in the corresponding packages. This architecture allows a weak coupling between classes and a strong internal consistency. This will make the code more solid. Also, this structure will limit Git conflicts and offer a better readability of the code.

* The `business_object` package contains our 13 modules corresponding to the 13 business object classes. 
* The modules of the `service` package import those of the DAO package to manage the persistence of user actions. Our service package classes also use those of the web package.  
* The `web` package contains at least one search module to access our back-end server.  
* The `view` package imports services to call business functionality. We will have one module per view. In particular, the abstract_vue module containing the AbstractView class will provide a template for the view classes that inherit from it. It will contain abstract methods for handling console display, menus and options.  
* The `test` package will contain a test module for each layer of our application. :smile:


<p align="right">(<a href="#top">Back to top</a>)</p>

### Used when implementing the code

This section will present our development tools.

* [Visual Studio Code](https://code.visualstudio.com/)

<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- MISE EN PLACE -->
## Setting up

Here is a way to install our application locally.
To run a local copy, follow these steps.

### Installation

1. Get a key for the API [https://www.dnd5eapi.co/](https://www.dnd5eapi.co/)
2. Clone the repository
   ```sh
   git clone https://github.com/Julien-Sklarik/Dragons-Unfurled.git 
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
   or
   ```
   pip install requests
   pip install psycopg2-binary
   pip install PyInquirer
   ```
4. Enter in the API `config.js`
   ```js
   const API_KEY = 'D&D 5e API';
   ```

### Accessing the application :

For a first use of our application, the following steps have to be done:
- 1: Open the VS Code terminal
- 2: Execute the SQL script [init_base.sql] to create the database tables (db),

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