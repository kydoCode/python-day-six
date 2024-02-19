import tkinter as tk
# Class joueur

class Joueur:
    # Constructeur se lance dès qu'on instancie la classe
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie # points de vie
        self.attaque = attaque # les points d'attaque
    
  #  def attack(self):
  #      self.vie 
        
    def attaquer(self, ennemi):    
        ennemi.vie -= self.attaque

class Ennemi:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie 
        self.attaque = attaque 
    
    def attaquer(self, joueur):
        joueur.vie -= self.attaque


fenetre = tk.Tk()
fenetre.title("Mini RPG - by Kydo")
fenetre.geometry("1024x768")

# Un joueur attaque, l'autre réplique

joueur = Joueur("Héro", 100, 10)
ennemi = Ennemi("Monstre", 50, 5)



fenetre.mainloop()