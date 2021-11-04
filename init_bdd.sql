CREATE TABLE Entité(
    id_entite serial PRIMARY KEY NOT NULL,
    nom_entite text NOT NULL,
    niveau int NOT NULL, 
    experience int NOT NULL,
    force int NOT NULL, 
    intelligence int NOT NULL,
    charisme int NOT NULL,
    dexterite int NOT NULL,
    constitution int NOT NULL, 
    sagesse int NOT NULL, 
    vie int NOT NULL,
    description text NOT NULL, 
    classe_armure int NOT NULL
); 

CREATE TABLE Campagne(
    id_campagne text PRIMARY KEY NOT NULL, 
    nom_campagne text NOT NULL
);


CREATE TABLE Donjon(
    id_donjon text PRIMARY KEY NOT NULL,
    nom_donjon text NOT NULL, 
    id_campagne text NOT NULL,
	FOREIGN KEY (id_donjon) REFERENCES Donjon(id_donjon)
);

CREATE TABLE Capacité(
    id_entite serial PRIMARY KEY NOT NULL, 
    nom_capacite text NOT NULL
); 

CREATE TABLE Langage(
    id_entite serial PRIMARY KEY NOT NULL, 
    nom_langage text NOT NULL
);

CREATE TABLE Attaque(
    id_entite serial PRIMARY KEY NOT NULL, 
    nom_attaque text NOT NULL   
);

CREATE TABLE Personnage(
    id_entite serial PRIMARY KEY NOT NULL,
    classe text NOT NULL,
    race text NOT NULL, 
    lore text NOT NULL
);

CREATE TABLE Monstre(
    id_entite text PRIMARY KEY NOT NULL,
    type text NOT NULL
);

CREATE TABLE Objet(
    id_objet text PRIMARY KEY NOT NULL, 
    nom_objet text NOT NULL, 
    description text NOT NULL
);

CREATE TABLE Salle(
    id_salle text PRIMARY KEY NOT NULL,
    nom_salle text NOT NULL,
    coordonnee_salle_x int NOT NULL, 
    coordonnee_salle_y int NOT NULL,
    id_donjon text NOT NULL,
	FOREIGN KEY (id_donjon) REFERENCES Donjon(id_donjon)
);

CREATE TABLE Cellule
(
    id_cellule text NOT NULL PRIMARY KEY , 
    coordonnee_cellule_x int NOT NULL,
    coordonnee_cellule_y int NOT NULL, 
    id_salle text NOT NULL,
	FOREIGN KEY (id_salle) REFERENCES Salle(id_salle)
);


CREATE TABLE Combat(
    id_jet text PRIMARY KEY NOT NULL,
    id_entite1 text NOT NULL,
    id_entite2 text NOT NULL,
	FOREIGN KEY (id_entite1) REFERENCES Entité(id_entite),
	FOREIGN KEY (id_entite2) REFERENCES Entité(id_entite)
);

CREATE TABLE Utilisateur(
    username text PRIMARY KEY NOT NULL, 
    est_administrateur boolean NOT NULL, 
    password text NOT NULL
);

CREATE TABLE Jet(
    id_jet text PRIMARY KEY NOT NULL, 
    resultat int NOT NULL, 
    revelation boolean NOT NULL, 
	username text NOT NULL, 
	FOREIGN KEY (username) REFERENCES Utilisateur(username)
);

CREATE TABLE FeedBack(
    id_feedback text PRIMARY KEY NOT NULL, 
    message text NOT NULL, 
    date_ecriture date NOT NULL, 
	username text NOT NULL,
	FOREIGN KEY (username) REFERENCES Utilisateur(username)
); 

CREATE TABLE Utilisateur_Entité(
    username text NOT NULL,
    id_entite text NOT NULL,
	PRIMARY KEY (username,id_entite),
	FOREIGN KEY (username) REFERENCES Utilisateur(username),
	FOREIGN KEY (id_entite) REFERENCES Entité(id_entite)
);

CREATE TABLE Utilisateur_Campagne(
    username text NOT NULL,
    id_entite text NOT NULL,
    est_joueur boolean NOT NULL,
	PRIMARY KEY (username, id_entite),
	FOREIGN KEY (username) REFERENCES Utilisateur(username),
	FOREIGN KEY (id_entite) REFERENCES Entité(id_entite)
);

CREATE TABLE Salle_Objet(
    id_salle text NOT NULL,
    id_objet text NOT NULL,
	PRIMARY KEY (id_salle, id_objet),
	FOREIGN KEY (id_salle) REFERENCES Salle(id_salle),
	FOREIGN KEY (id_objet) REFERENCES Objet(id_objet)
);

CREATE TABLE Entité_Objet(
    id_entite text NOT NULL,
    id_objet text NOT NULL,
	PRIMARY KEY (id_entite, id_objet),
	FOREIGN KEY (id_entite) REFERENCES Entité(id_entite),
	FOREIGN KEY (id_objet) REFERENCES Objet(id_objet)
);