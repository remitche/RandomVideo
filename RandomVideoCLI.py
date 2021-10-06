#import des modules
import os
import module
import subprocess
import random

#Chargement des données
path = os.getcwd()
listFiles = []

#Debut du programme
print("Lancement de la recherche ...")
print("Dossier en cours : " + path)

listFiles = module.searchTroughFolder()

retourFonction = module.chooseRandomFile(listFiles)
