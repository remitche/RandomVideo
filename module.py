import os
import module
import subprocess
import random


def helloModule():
    print("Hello i'am a module")

infos = {
    "name" : "module de test",
    "description" : "Test de module"
}

listesExtensions = [
    ".avi",
    ".mpeg",
    ".mpg",
    ".MP4",
    ".mov"
]

#Fonction qui cherche à travers un chemin donné
def searchTroughFolder(path =""):
    listFiles = []
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            root, extension = os.path.splitext(name)
            if extension in module.listesExtensions:
                listFiles.append(name)
    print(str(len(listFiles)) + " fichiers trouvé(s)")
    return listFiles

#Fonction qui choisi de façon aléatoire
def chooseRandomFile(listFiles):
    #Lancement du fichier si au moins un a été trouvé
    if(len(listFiles) > 0):
        fileChosen = listFiles[random.randint(0, len(listFiles)- 1)]
        print("Lanchement de : " + fileChosen)
        os.startfile(fileChosen)
        return fileChosen
    else:
        print("Rien trouvé :(")
        return False
