CREATE TABLE Entite(
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
    id_campagne serial PRIMARY KEY NOT NULL, 
    nom_campagne text NOT NULL
);


CREATE TABLE Donjon(
    id_donjon serial PRIMARY KEY NOT NULL,
    nom_donjon text NOT NULL, 
    id_campagne serial NOT NULL,
	FOREIGN KEY (id_donjon) REFERENCES Donjon(id_donjon)
);

CREATE TABLE Capacite(
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
    id_entite serial PRIMARY KEY NOT NULL,
    type text NOT NULL
);

CREATE TABLE Objet(
    id_objet serial PRIMARY KEY NOT NULL, 
    nom_objet text NOT NULL, 
    description text NOT NULL
);

CREATE TABLE Salle(
    id_salle serial PRIMARY KEY NOT NULL,
    nom_salle text NOT NULL,
    coordonnee_salle_x int NOT NULL, 
    coordonnee_salle_y int NOT NULL,
    id_donjon serial NOT NULL,
	FOREIGN KEY (id_donjon) REFERENCES Donjon(id_donjon)
);

CREATE TABLE Cellule
(
    id_cellule serial NOT NULL PRIMARY KEY , 
    coordonnee_cellule_x int NOT NULL,
    coordonnee_cellule_y int NOT NULL, 
    id_salle serial NOT NULL,
	FOREIGN KEY (id_salle) REFERENCES Salle(id_salle)
);


CREATE TABLE Combat(
    id_jet serial PRIMARY KEY NOT NULL,
    id_entite1 int NOT NULL,
    id_entite2 int NOT NULL,
	FOREIGN KEY (id_entite1) REFERENCES Entite(id_entite),
	FOREIGN KEY (id_entite2) REFERENCES Entite(id_entite)
);

CREATE TABLE Utilisateur(
    username text PRIMARY KEY NOT NULL, 
    est_administrateur boolean NOT NULL, 
    password text NOT NULL
);

CREATE TABLE Jet(
    id_jet serial PRIMARY KEY NOT NULL, 
    resultat int NOT NULL, 
    revelation boolean NOT NULL, 
	username text NOT NULL, 
	FOREIGN KEY (username) REFERENCES Utilisateur(username)
);

CREATE TABLE FeedBack(
    id_feedback serial PRIMARY KEY NOT NULL, 
    message text NOT NULL, 
    date_ecriture date NOT NULL, 
	username text NOT NULL,
	FOREIGN KEY (username) REFERENCES Utilisateur(username)
); 

CREATE TABLE Utilisateur_Entite(
    username text NOT NULL,
    id_entite serial NOT NULL,
	PRIMARY KEY (username,id_entite),
	FOREIGN KEY (username) REFERENCES Utilisateur(username),
	FOREIGN KEY (id_entite) REFERENCES Entite(id_entite)
);

CREATE TABLE Utilisateur_Campagne(
    username text NOT NULL,
    id_entite serial NOT NULL,
    est_joueur boolean NOT NULL,
	PRIMARY KEY (username, id_entite),
	FOREIGN KEY (username) REFERENCES Utilisateur(username),
	FOREIGN KEY (id_entite) REFERENCES Entite(id_entite)
);

CREATE TABLE Salle_Objet(
    id_salle serial NOT NULL,
    id_objet serial NOT NULL,
	PRIMARY KEY (id_salle, id_objet),
	FOREIGN KEY (id_salle) REFERENCES Salle(id_salle),
	FOREIGN KEY (id_objet) REFERENCES Objet(id_objet)
);

CREATE TABLE Entite_Objet(
    id_entite serial NOT NULL,
    id_objet serial NOT NULL,
	PRIMARY KEY (id_entite, id_objet),
	FOREIGN KEY (id_entite) REFERENCES Entite(id_entite),
	FOREIGN KEY (id_objet) REFERENCES Objet(id_objet)
);