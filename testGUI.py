import os
import module
import subprocess
import random
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
#Globals Vars
globalListFiles = []

#Bouttons
def button_clicked():
    print("boutonclické")
#
#   Début du programme
#
#Fenetre 

#création de l'objet tkinter qui gère la fenetre
root = tk.Tk()
root.title('RandomVideo')#nom
root.geometry('600x400+50+50')#taille width - height - paddingx - paddingy



#Création du bouton de selection de dossier
button = ttk.Button(root, text="Select ", command=button_clicked)
button.pack()

#affichage de la fenètre
root.mainloop()


