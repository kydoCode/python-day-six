import tkinter as tk
from tkinter import Tk, Button

# Interaction avec les widgets

def afficher_mesage():
    print("Vous avez cliqué sur le bouton !")

fenetre = Tk()
fenetre.title("Tkinter v1.0 - Cours LP(2) - 19022024")

bouton = Button(fenetre, text="Cliquez ici", command=afficher_mesage)
bouton.pack()

# Interaction avec une zone de texte

def afficher_texte(event): #e
    contenu = zone_texte.get("1.0", tk.END)


fenetre.mainloop()