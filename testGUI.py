# from tkinter import Tk
import tkinter as tk

# fenetre = Tk()
fenetre = tk.Tk()

fenetre.title("Ma première fenêtre Tkinter")

# 
etiquette = tk.Label(fenetre, text="Autre texte")
etiquette.pack()

#Création d'une liste déroulante 
listbox = tk.Listbox(fenetre)
listbox.pack() # permet de passer à l'affichage

#Ajouter d'éléments à la liste déroulante
listbox.insert(tk.END, "Elément 1")
listbox.insert(tk.END, "Elément 2")
listbox.insert(tk.END, "Elément 3")

##Checkbutton

case_cocher_var = tk.IntVar()

# Création d'une case à cocher

case_cocher = tk.Checkbutton(fenetre, text="Cocher", variable=case_cocher_var)
case_cocher.pack()

fenetre.mainloop() # Toujours la dernière ligne 