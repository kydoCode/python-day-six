# from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image # pour importer des images dans d'autre format

# Création d'une instance de la classe Tk, qui représente la fenêtre principale de l'application
# fenetre = Tk()
fenetre = tk.Tk()

# Définition du titre de la fenêtre principale comme "".
fenetre.title("Tkinter v1.0 - Cours LP - 19022024")

# 
etiquette = tk.Label(fenetre, text="Autre texte")
etiquette.grid(row=0, column=0)

#Création d'une liste déroulante 
listbox = tk.Listbox(fenetre)
listbox.grid(row=0, column=1) # permet de passer à l'affichage

#Ajouter d'éléments à la liste déroulante
listbox.insert(tk.END, "Elément 1")
listbox.insert(tk.END, "Elément 2")
listbox.insert(tk.END, "Elément 3")

##Checkbutton

case_cocher_var = tk.IntVar()

# Création d'une case à cocher

case_cocher = tk.Checkbutton(fenetre, text="Cocher", variable=case_cocher_var)
case_cocher.grid(row=0, column=2)

## Radiobutton

# Variable pour stocker la sélection du bouton radio

selection_var = tk.StringVar()

# Création de boutons radio

bouton_radio1 = tk.Radiobutton(fenetre, text="Option 1", variable=selection_var, value="Option 1")
bouton_radio1.grid(row=1, column=0)

bouton_radio2 = tk.Radiobutton(fenetre, text="Option 2", variable=selection_var, value="Option 2")
bouton_radio2.grid(row=1, column=1)

# deselect_all()

## Combobox

# Création d'une combobox
combobox = ttk.Combobox(fenetre)
combobox.grid(row=1, column=2)

#Ajout d'éléments à la combobox
combobox['values'] = ('Option 1', 'Option 2', 'Option 3')

#Place: référence en haut à gauche, valeur en x et y.

etiquette1 = tk.Label(fenetre, text="Place test 1")

etiquette1.place(x=150,y=150)

# Création d'un bouton avec une couleur de fond personnalisée

bouton = tk.Button(fenetre, text="Clic et clac", bg="#c1c1c1", fg="blue")
bouton.place(x=250, y=300)

# Création d'une étiquette avec une police personnalisée
etiquette = tk.Label(fenetre, text="Bonjour, Tkinter!", font=("Arial", 14))
etiquette.grid(row=2, column=0)

etiquette = tk.Label(fenetre, text="Etiquette 2", font=("Lato", 14))
etiquette.grid(row=2, column=1)

## Les polices: ajout

# Chemin vers le fichier de police téléchargé
# chemin_police = "chemin_vers_la_police/Lato_Regular.ttf"
chemin_police = "ProtestRevolution-Regular.ttf"
# "fonts/Anta/Anta-Regular.ttf"

# Chargement de la police personnalisée
police_protest = font.Font(family="ProtestRevolution-Regular", size=16, weight="normal")
# Assurez vous de spécificer le nom correct de la police en utilisant le mêùe nom que le fichier téléchargé

#Création d'une étiquette avec la police personnalisée
etiquette = tk.Label(fenetre, text="Test de font ProtestRevolution", font=police_protest)
etiquette.grid(row=2, column=2)

## Les bordures

# Création d'un cadre avec une bordure personnalisée
cadre = tk.Frame(fenetre, bd=8, relief="sunken")
cadre.grid(row=3,column=0,columnspan=2)

#Ajout d'un bouton dans le cadre
bouton = tk.Button(cadre, text="Click ici")
bouton.grid(row=3,column=1)

## Les images

#Chargement d'une image

image = tk.PhotoImage(file="logo.jpeg")

# Création d'un bouton avec une image
bouton = tk.Button(fenetre, image=image)
bouton.grid(raw=3, column=2)

## pip install Pillow

image = ImageTk.PhotoImage(Image.open("logo.jpeg"))

## Création d'un widget Label pour afficher l'image

label_image = tk.Label(fenetre, image=image)
label_image.grid(raw=4, column=0)

fenetre.mainloop() # Toujours la dernière ligne 