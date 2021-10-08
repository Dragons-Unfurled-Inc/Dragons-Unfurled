from abc import ABC, abstractmethod


class Entite(ABC): 
    def __init__(self,nom,taille, alignement, armure, hit_points, hit_dice, vitesse, force, dextérité, constitution, intelligence, sagesse, charisme,compétences, langages, experience):
        self.nom = nom
        self.taille = taille 
        self.alignement = alignement 
        self.armure = armure 
        self.hit_points = hit_points
        self.hit_dice = hit_dice
        self.vitesse = vitesse 
        self.force = force 
        self.dextérité = dextérité 
        self.constitution = constitution
        self.intelligence = intelligence 
        self.sagesse = sagesse 
        self.charisme = charisme 
        self.compétences = compétences
        self.langages = langages
        self.experience = experience 

    
