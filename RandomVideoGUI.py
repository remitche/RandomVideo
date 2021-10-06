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
    folderChosen = fd.askdirectory()
    labelDossier = ttk.Label(root, text =folderChosen)
    labelDossier.pack()
    listFiles = module.searchTroughFolder()
    globalListFiles=  listFiles
    retourFonction = module.chooseRandomFile(listFiles)
    if(retourFonction != False):
        labelResultat = ttk.Label(root, text="Lancement de " + retourFonction)
    else:
        labelResultat = ttk.Label(root, text="Aucun fichier trouvé :( ")
    labelResultat.pack()

def button_goRandom():
    retourFonction = module.chooseRandomFile(globalListFiles)
    if(retourFonction != False):
        button.text = ttk.Label(root, text="Lancement de " + retourFonction)
    else:
        button.text = "Aucun fichier trouvé :( "
#
#   Début du programme
#
#Fenetre 

#création de l'objet tkinter qui gère la fenetre
root = tk.Tk()
root.title('RandomVideo')#nom
root.geometry('600x400+50+50')#taille width - height - paddingx - paddingy

# place a label on the root window
message = ttk.Label(root, text="Select a folder")
message.pack()

#Création du bouton de selection de dossier
button = ttk.Button(root, text="Select ", command=button_clicked)
button.pack()

#Création du bouton de lancement du random
button2 = ttk.Button(root, text="Go Random File ", command=button_goRandom)
button2.pack()

#affichage de la fenètre
root.mainloop()


